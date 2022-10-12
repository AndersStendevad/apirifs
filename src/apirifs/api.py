""" FastAPI"""

import pandas as pd

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBearer
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.responses import Response

from apirifs.models import Run, Metric, Status
from apirifs.settings import Settings
from apirifs.store import Store

settings = Settings()
security = HTTPBearer()
secret_key = settings.security_admin_password

runs_store = Store("runs")
status_store = Store("status")

app = FastAPI()
app.add_middleware(HTTPSRedirectMiddleware)


def api_key_auth(api_key: str = Depends(security)):
    if api_key.credentials != secret_key.get_secret_value():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="UNAUTHORIZED"
        )


@app.get("/")
@app.get("/health")
async def healthcheck():
    """Healthcheck endpoint"""
    return 200


@app.post("/metric", status_code=201, dependencies=[Depends(api_key_auth)])
def create_metric(metric: Metric):
    """Create metric endpoint

    Parameters
    ----------
    metric : Metric
        Metric object

    Returns
    -------
    response: str
        Response in json format
    status_code: int
        Status code
    """
    key = metric.step
    value = metric.dict()
    metrics = Store(metric.run_id)
    metrics.insert(key, value)
    return status.HTTP_201_CREATED


@app.post("/run", status_code=201, dependencies=[Depends(api_key_auth)])
def create_run(run: Run):
    """Create run endpoint

    Parameters
    ----------
    run : Run
        Run object

    Returns
    -------
    response: str
        Response in json format
    status_code: int
        Status code
    """
    key = run.run_id
    value = run.dict()
    runs_store.insert(key, value)
    return status.HTTP_201_CREATED


@app.get("/objects", dependencies=[Depends(api_key_auth)])
def get_objects():
    """Grafana search endpoint

    Returns
    -------
    response: List
        Response list of objects
    """
    return ["run", "runs", "run_ids", "metrics", "status"]


@app.get("/runs", dependencies=[Depends(api_key_auth)])
def runs():
    """Grafana query endpoint

    Returns
    -------
    response: List
        Response in list of json
    """
    return runs_store.values()


@app.get("/runs_ids", dependencies=[Depends(api_key_auth)])
def runs_ids():
    """Grafana query endpoint

    Returns
    -------
    response: List
        Response in list of ids
    """
    return runs_store.keys()


@app.get("/run/{run_id}", dependencies=[Depends(api_key_auth)])
def get_run(run_id: str):
    """Grafana query endpoint

    Returns
    -------
    response: List
        Response in list of json
    """
    metrics = Store(run_id)
    return metrics.values()

@app.delete("/run/{run_id}", dependencies=[Depends(api_key_auth)])
def delete_run(run_id: str):
    """Delete run from runs. But do not delete metrics

    """
    del runs_store[run_id]
    return status.HTTP_204_NO_CONTENT


@app.get("/csv/runs", dependencies=[Depends(api_key_auth)])
def csv_runs():
    """Grafana query endpoint

    Returns
    -------
    response: str
        csv
    """

    df = pd.DataFrame(runs_store.values())
    if not df.empty:
        df = df.sort_values(by=['start_time'], ascending=False)
    else:
        df = pd.DataFrame(columns=Run.__fields__.keys())
    return Response(content=df.to_csv(index=False), media_type="text/csv")


@app.get("/csv/runs/{run_id}", dependencies=[Depends(api_key_auth)])
def csv_run(run_id: str):
    """Grafana query endpoint

    Returns
    -------
    response: str
        csv
    """
    metrics = Store(run_id)
    df = pd.DataFrame(metrics.values())
    if not df.empty:
        if "step" in df.columns:
            df = df.sort_values(by=['step'])
        else:
            df = df.sort_values(by=['epoch'])
    else:
        df = pd.DataFrame(columns=Metric.__fields__.keys())
    return Response(content=df.to_csv(index=False), media_type="text/csv")

@app.post("/status", status_code=201, dependencies=[Depends(api_key_auth)])
def create_status(status_object: Status):
    """Create status endpoint

    Parameters
    ----------
    status_object : Status
        Status object

    Returns
    -------
    response: str
        Response in json format
    status_code: int
        Status code
    """
    key = status_object.run_id
    value = status_object.dict()
    status_store.insert(key, value)
    return status.HTTP_201_CREATED

@app.get("/csv/status/{run_id}", dependencies=[Depends(api_key_auth)])
def csv_status(run_id: str):
    """Grafana query endpoint

    Returns
    -------
    response: str
        csv
    """
    df = pd.DataFrame(status_store.values())
    if not df.empty:
        df = df.loc[df['run_id'] == run_id]
        df = df.drop(columns=["run_id"])
    else:
        df = pd.DataFrame(columns=Status.__fields__.keys())
    return Response(content=df.to_csv(index=False), media_type="text/csv")


