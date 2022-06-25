import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

matplotlib.use('TkAgg')

def drawState(state):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')
    plt.pcolormesh(state, cmap=plt.get_cmap('binary'))
    plt.axis('off')
    plt.show()


def animateStates(states, name):
    # For a better viewing experience
    lastState = states[len(states)-1]
    for i in range(int(len(states)/10)):
        states.append(lastState)

    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')
    plt.axis('off')
    p = plt.pcolormesh(states[0], cmap=plt.get_cmap('binary'))

    def update(i):
        p.set_array(states[i])
        return p

    ani = animation.FuncAnimation(
        fig, update, frames=range(0, len(states), 1), interval=10)
    ani.save(name + '.gif', animation.PillowWriter(fps=20))
    ani.save(name + '.mp4', animation.FFMpegWriter(fps=20))