from src import api

# 0.0.0.0 is used to allow passthrough in a virtual machine for dev
if __name__ == "__main__":
    api.go_fast(host="0.0.0.0")
