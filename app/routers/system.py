from fastapi import APIRouter

router = APIRouter(tags=["Système"])


@router.get("/health", summary="Vérifier que l'API répond")
def health():
    # Route de test : permet au front de vérifier que le back tourne
    return {"status": "ok", "version": "0.1.0"}