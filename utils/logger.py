import logging
import pathlib
from datetime import datetime

#crea carpta logs
logs_dir = pathlib.Path("logs")

#si existe no la crea
logs_dir.mkdir(exist_ok=True)

#capturo fecha para colocarlo en las carpetas
timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
#configuro login
logging.basicConfig(
    
    #aca le digo que cree el log
    filename= logs_dir / f"log_{timestamp}.log",
    
    #le digo que tipo de parametro es lo que se creo
    level=logging.INFO,
    
    #formato las s sirven como un marcador, lo usa para reemplazarlos valores automaticamente
    format= "%(asctime)s %(levelname)s %(name)s - %(message)s",
    
    #obliga a python a usar este formato
    force=True
)
#llamo al logger y lo creo
logger = logging.getLogger("talento tech")

