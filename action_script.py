import json
import os
from datetime import datetime

# Ruta del archivo de log
log_file = "execution_log.json"

# Datos de la ejecución
execution_data = {
    "timestamp": datetime.now().isoformat(),
    "files_in_repo": len([f for f in os.listdir(".") if os.path.isfile(f)]),
    "action": "Automated workflow execution"
}

# Leer el log existente o crear uno nuevo
if os.path.exists(log_file):
    with open(log_file, "r") as f:
        log = json.load(f)
else:
    log = []

# Añadir la nueva ejecución
log.append(execution_data)

# Guardar el log actualizado
with open(log_file, "w") as f:
    json.dump(log, f, indent=2)

print(f"✅ Ejecución registrada: {execution_data['timestamp']}")
print(f"📊 Total de archivos en el repo: {execution_data['files_in_repo']}")
