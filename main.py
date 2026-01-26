import subprocess

def run(cmd, workdir):
    subprocess.Popen(
        ["cmd", "/k", cmd],
        cwd=workdir,
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

run(
    "bin\\kc.bat start-dev --http-port=8081",
    r"C:\Users\maiba\Downloads\keycloak-26.5.2\keycloak-26.5.2"
)
