from fastapi.responses import JSONResponse
from fastapi import status
import django_fastapi.utils.constants as constants

def root_health_path(_app) -> None:
    """
    Define root and health check endpoints for the FastAPI application.

    Args:
        _app (FastAPI): The FastAPI application instance.
    """

    @_app.get("/", include_in_schema=False)
    def root() -> JSONResponse:
        """
        Root endpoint.

        Returns:
            JSONResponse: A JSON response with a success message.
        """
        return JSONResponse(
            status_code=status.HTTP_200_OK, content={"message": constants.SUCCESS}
        )

    @_app.get("/healthcheck", include_in_schema=False)
    def healthcheck() -> JSONResponse:
        """
        Health check endpoint.

        Returns:
            JSONResponse: A JSON response with a success message.
        """
        return JSONResponse(
            status_code=status.HTTP_200_OK, content={"message": constants.SUCCESS}
        )
