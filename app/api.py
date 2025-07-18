# app/api.py

from fastapi import APIRouter, HTTPException
from app.models import FibonacciRequest
from app.logic import fibonacci
from app.models import PowRequest
from app.logic import pow_custom
from app.models import FactorialRequest
from app.logic import factorial_custom

router = APIRouter()

@router.post("/fibonacci")
def compute_fibonacci(payload: FibonacciRequest):
    try:
        result = fibonacci(payload.n)
        return {"n": payload.n, "fibonacci": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/pow")
def compute_pow(payload: PowRequest):
    result = pow_custom(payload.base, payload.exponent)
    return {
        "base": payload.base,
        "exponent": payload.exponent,
        "result": result
    }

@router.post("/factorial")
def compute_factorial(payload: FactorialRequest):
    result = factorial_custom(payload.n)
    return {
        "n": payload.n,
        "result": result
    }