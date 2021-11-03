import matplotlib.pyplot as plt


def create_rect(x0, y0, w, h):
    return [
        [x0, y0, x0, y0 + h],
        [x0, y0 + h, x0 + w, y0 + h],
        [x0 + w, y0 + h, x0 + w, y0],
        [x0 + w, y0, x0, y0]
    ]


walls = [
    [1, 1, 1, 4],
    [3, 1, 3, 3],
    [2, 1, 2, 3],
    [1, 4, 6, 4],
]

rect = create_rect(4, 2, 2, 1)
for wa in rect:
    walls.append(wa)

for i in range(len(walls)):
    plt.plot([walls[i][0], walls[i][2]], [walls[i][1], walls[i][3]], 'b')
plt.show()
