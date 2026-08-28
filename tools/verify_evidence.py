#!/usr/bin/env python3
from __future__ import annotations
import base64, hashlib, json, sys, fnmatch
from pathlib import Path
try:
    from cryptography.hazmat.primitives.serialization import load_pem_public_key
except Exception:
    print('Missing dependency: cryptography')
    sys.exit(2)
ROOT=Path(__file__).resolve().parents[1]
checks=0; fails=[]
def check(name, cond):
    global checks
    checks+=1
    if not cond: fails.append(name)
def loadj(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def cbytes(o): return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')
def jhash(o): return hashlib.sha256(cbytes(o)).hexdigest()
def shastr(s): return hashlib.sha256(s.encode()).hexdigest()
def verify_sig(obj,pub):
    core=dict(obj); sig=core.pop('cp_signature',None)
    if not sig: return False
    try:
        pad=sig+'='*((4-len(sig)%4)%4)
        pub.verify(base64.urlsafe_b64decode(pad),cbytes(core)); return True
    except Exception: return False
pub=load_pem_public_key((ROOT/'evidence/public-run/cp_public.pem').read_bytes())
summary=loadj(ROOT/'evidence/observed-summary.json')
for rec in summary:
    check(rec['id']+': status', rec['status']=='PASS')
    check(rec['id']+': decision', rec['observed_decision']==rec['expected_decision'])
    check(rec['id']+': reason', rec['observed_reason_code']==rec['expected_reason_code'])

scroot=ROOT/'evidence/public-run/scenarios'
for d in sorted(p for p in scroot.iterdir() if p.is_dir()):
    req=loadj(d/'request.json'); obs=loadj(d/'observed.json'); chain=[json.loads(x) for x in (d/'artifact_log.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]; authreg=loadj(d/'authority_registry.json'); scopes=loadj(d/'scope_registry.json'); pol=loadj(d/'policy_registry.json')
    # all intents present in request hash correctly
    ei=req['execution_intent']; core={k:ei[k] for k in ['intent_id','principal_id','function','target','params_c14n','timestamp']}; check(d.name+': intent_hash',jhash(core)==ei['intent_hash'])
    # scope hashes
    for sid,se in scopes.items():
        tmp={k:v for k,v in se.items() if k!='scope_hash'}; check(d.name+f': scope_hash:{sid}', jhash(tmp)==se['scope_hash'])
    # permit signatures in request/propose where present
    permits=[]
    for k in ['permit','original_permit','tampered_permit']:
        if isinstance(req.get(k),dict): permits.append((k,req[k]))
    for k,v in obs.items():
        if isinstance(v,dict) and isinstance(v.get('permit'),dict): permits.append((k+'.permit',v['permit']))
    seen=set()
    for label,p in permits:
        sigkey=(p.get('permit_id'),p.get('cp_signature'),p.get('nonce'))
        if sigkey in seen: continue
        seen.add(sigkey)
        ok=verify_sig(p,pub)
        if 'tampered_permit' in label: check(d.name+': tampered permit signature fails',not ok)
        else: check(d.name+': '+label+' signature',ok)
    # artifact chain integrity and snapshot hashes
    prev=hashlib.sha256(b'genesis').hexdigest()
    for i,e in enumerate(chain):
        aa=e['artifact']; snaps=e.get('snapshots',{})
        check(d.name+f': artifact[{i}] signature',verify_sig(aa,pub))
        check(d.name+f': artifact[{i}] chain',aa['prev_artifact_hash']==prev)
        check(d.name+f': artifact[{i}] policy',aa['policy_hash']==snaps.get('policy',{}).get('current_hash',''))
        check(d.name+f': artifact[{i}] authority',aa['authority_state_hash']==jhash(snaps.get('ar',{})))
        if snaps.get('se'):
            check(d.name+f': artifact[{i}] scope',aa['scope_hash']==snaps['se'].get('scope_hash',''))
        result=snaps.get('result'); expected=jhash(result) if result is not None else shastr('null'); check(d.name+f': artifact[{i}] result',aa['result_hash']==expected)
        prev=jhash(aa)

# schema files must parse and preserve exact expected decision enum / reason-code set
for p in (ROOT/'schemas').glob('*.json'):
    try: loadj(p); check('schema parse:'+p.name,True)
    except Exception: check('schema parse:'+p.name,False)
aa_schema=loadj(ROOT/'schemas/admission_artifact.schema.json')
check('schema decisions ADMIT/DENY only',aa_schema['properties']['decision']['enum']==['ADMIT','DENY'])
expected_codes={'OK','NO_PERMIT','SIG_FAIL','EXPIRED','REVOKED','SCOPE_FAIL','INTENT_MISMATCH','POLICY_MISMATCH','REPLAY','AUTHORITY_NOT_ACTIVE','AUTHORITY_EXPIRED','INTERNAL_ERROR'}
check('schema reason codes',set(aa_schema['properties']['reason_code']['enum'])==expected_codes)

if fails:
    print(f'Public evidence verification: {checks-len(fails)}/{checks} PASS')
    for f in fails: print('FAIL:',f)
    sys.exit(1)
print(f'Public evidence verification: {checks}/{checks} PASS')
print('Scope: controlled synthetic evidence from the final MVP package; not production or independent external reproduction.')
