def read_iris_data():
    raw_data = []
    labels = {}
    label_index = 0
    with open('./datasets/iris.data') as f:
        for line in f:
            if len(line)==1:
                continue
            data = line.split(',')
            data[-1] = data[-1][:-1]
            for i in range(len(data)-1):
                data[i] = float(data[i])
            if data[-1] not in labels:
                labels[data[-1]] = label_index
                label_index += 1
            data[-1] = labels[data[-1]]
            raw_data.append(data)
    return raw_data, labels




