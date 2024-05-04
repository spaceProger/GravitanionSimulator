from classes.SimulationClass import Simulation


if __name__ == "__main__":
    simulation = Simulation(screen_size=(1500, 1000), fps=60)
    simulation.run()
