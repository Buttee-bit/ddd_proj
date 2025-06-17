import asyncio
from functools import wraps
from opentelemetry import trace

def trace_custom(name: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            tracer = trace.get_tracer(__name__)
            with tracer.start_as_current_span(f"{name}"):
                if asyncio.iscoroutinefunction(func):
                    return func(*args, **kwargs)
                else:
                    return func(*args, **kwargs)
        return wrapper
    return decorator