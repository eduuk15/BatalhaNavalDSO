import sys
print(sys.path)
sys.path.append("../")


from controllers.controllerMain import ControllerMain

if __name__ == "__main__":
    ControllerMain().inicializa_sistema()