""" FastAPI"""

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBearer
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

from apirifs.models import Run, Metric
from apirifs.settings import Settings

settings = Settings()
security = HTTPBearer()
secret_key = settings.security_admin_password

app = FastAPI()
app.add_middleware(HTTPSRedirectMiddleware)

def api_key_auth(api_key: str = Depends(security)):
    if api_key.credentials != secret_key.get_secret_value():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="UNAUTHORIZED"
        )


@app.get("/health")
async def healthcheck():
    """Healthcheck endpoint"""
    return 200


@app.post("/metric", status_code=201, dependencies=[Depends(api_key_auth)])
async def create_metric(metric: Metric): 
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

    print(metric)
    return status.HTTP_201_CREATED

@app.post("/run", status_code=201, dependencies=[Depends(api_key_auth)])
async def create_run(run: Run): 
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

    print(run)
    return status.HTTP_201_CREATED

