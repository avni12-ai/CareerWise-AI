import sys
from app import app
from expert_system.knowledge_base import PRESET_PROFILES

client = app.test_client()

print("=== 1. Testing GET / ===")
res = client.get("/")
assert res.status_code == 200, f"Status {res.status_code}"
assert b"Intelligent Career Guidance" in res.data
print("OK: Home page renders successfully!")

print("\n=== 2. Testing GET /assessment ===")
res = client.get("/assessment")
assert res.status_code == 200, f"Status {res.status_code}"
assert b"Comprehensive Career Assessment" in res.data
print("OK: Assessment page renders successfully!")

print("\n=== 3. Testing POST /api/assess ===")
payload = {
    "student_name": "Test Aarav",
    "skills": PRESET_PROFILES["profile_ai"]["skills"],
    "interests": PRESET_PROFILES["profile_ai"]["interests"],
    "subjects": PRESET_PROFILES["profile_ai"]["subjects"],
    "work_style": PRESET_PROFILES["profile_ai"]["work_style"]
}
res = client.post("/api/assess", json=payload)
assert res.status_code == 200, f"Status {res.status_code}"
data = res.get_json()
assert data["success"] is True
top_1 = data["results"]["top_recommendations"][0]
print(f"OK: Top Recommendation is '{top_1['evaluation']['title']}' with score {top_1['evaluation']['composite_score']}% and CF {top_1['evaluation']['certainty_factor']}")

print("\n=== 4. Testing GET /results ===")
res = client.get("/results")
assert res.status_code == 200, f"Status {res.status_code}"
assert b"Career Advisory for" in res.data
print("OK: Results page renders with session data!")

print("\n=== 5. Testing GET /backward-chain & POST /api/backward-chain ===")
res = client.get("/backward-chain")
assert res.status_code == 200
bc_payload = {
    "target_career_id": "ai_ml_engineer",
    "skills": PRESET_PROFILES["profile_ai"]["skills"],
    "interests": PRESET_PROFILES["profile_ai"]["interests"],
    "subjects": PRESET_PROFILES["profile_ai"]["subjects"],
    "work_style": PRESET_PROFILES["profile_ai"]["work_style"]
}
res = client.post("/api/backward-chain", json=bc_payload)
assert res.status_code == 200
bc_data = res.get_json()
assert bc_data["success"] is True
print(f"OK: Backward chaining verdict: {bc_data['diagnosis']['verdict']['title']}")

print("\n=== 6. Testing GET /what-if & POST /api/what-if-simulate ===")
res = client.get("/what-if")
assert res.status_code == 200
res = client.post("/api/what-if-simulate", json=bc_payload)
assert res.status_code == 200
sim_data = res.get_json()
assert sim_data["success"] is True
print(f"OK: What-If simulation top 1: {sim_data['top_3'][0]['title']}")

print("\n=== 7. Testing GET /kb-explorer ===")
res = client.get("/kb-explorer")
assert res.status_code == 200
assert b"Knowledge Base Inspector" in res.data
print("OK: KB Explorer renders with all rules!")

print("\n=== 8. Testing GET /printable-report ===")
res = client.get("/printable-report")
assert res.status_code == 200
assert b"Official Evaluation" in res.data
print("OK: Printable report renders successfully!")

print("\n=======================================================")
print(" ALL 8 SYSTEM TESTS PASSED SUCCESSFULLY! (100% HEALTHY)")
print("=======================================================")
