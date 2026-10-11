from fastapi import FastAPI

app = FastAPI(title="Aegentis API", version="1.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to Aegentis API"}

@app.post("/api/v1/incidents")
def create_incident():
    return {"message": "Create an incident"}

@app.get("/api/v1/incidents")
def list_incidents():
    return {"data": []}

@app.get("/api/v1/incidents/{incident_id}")
def get_incident(incident_id: int):
    return {"id": incident_id, "status": "New"}

@app.get("/api/v1/environments")
def list_environments():
    return {"data": []}

@app.get("/api/v1/integrations")
def list_integrations():
    return {"data": []}

@app.get("/api/v1/policies")
def list_policies():
    return {"data": []}

@app.get("/api/v1/audit-events")
def list_audit_events():
    return {"data": []}
