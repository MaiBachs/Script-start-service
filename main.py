import subprocess

processes = [
    # start keycloack 18
    ("bin/kc.sh start-dev --http-port=8000",
     "/home/chuyenpn/Downloads/keycloak-18.0.0",
     "Keycloak 18"),
    # start keycloack 24
    ("bin/kc.sh start-dev --http-port=8002",
     "/home/chuyenpn/Downloads/keycloak-24.0.0",
     "Keycloak 24"),

    # start redis
    ("docker compose -f docker-compose-redis.yml up",
     "/home/chuyenpn/Downloads/idp_demo",
     "Redis single node"),

    # mount disk general
    ("sudo mkdir -p /nfs/general "
     "&& sudo mkdir -p /nfs/home "
     "&& sudo mount 10.1.111.34:/var/nfs/general /nfs/general "
     "&& sudo mount 10.1.111.34:/home /nfs/home "
     "&& df -h ",
     "/home/chuyenpn/Downloads/idp_demo",
     "Redis single node"),

    # start logstash
    ("./bin/logstash -f ./config/logstash-sample-41-5.conf",
     "/home/chuyenpn/Downloads/campaign-multi-service/elk_stack/logstash-8.17.0",
     "Logstash"),
    # start elasticsearch
    ("./bin/elasticsearch",
     "/home/chuyenpn/Downloads/campaign-multi-service/elk_stack/elasticsearch-8.17.0",
     "Elasticsearch"),
    # start kibana
    ("./bin/kibana",
     "/home/chuyenpn/Downloads/campaign-multi-service/elk_stack/kibana-8.17.0",
     "Elasticsearch"),

    # start orchestrator-be
    ("export NVM_DIR=\"$HOME/.nvm\" && "
     "[ -s \"$NVM_DIR/nvm.sh\" ] && . \"$NVM_DIR/nvm.sh\" && "
     "nvm use 18 && yarn start-backend",
     "/home/chuyenpn/Downloads/idp-click-ops/orchestrator",
     "Orchestrator-be"
     ),

    # start camunda server
    ("docker compose -f docker-compose.yml up",
     "/home/chuyenpn/Downloads/idp_demo/docker-compose-8.6",
     "camunda-server"),
]

for command, workdir, name in processes:
    subprocess.Popen([
        "gnome-terminal",
        "--title", name,
        "--working-directory", workdir,
        "--",
        "bash", "-c",
        f"{command}; exec bash"
    ])
