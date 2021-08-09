 
m = int(input("En que modulo desea trabajar:"))
keys = (input("Ingrese los valores seguidos de una coma:"))
keys = keys.split(',')

values = [None] * (m+1)

def get_index(key: str):
    return hash(key) % len(values)

def modulo(keys):
    values = []
    for i in range(len(keys)):
        keys[i] = int(keys[i])

    for key in keys:
        key = key % m
        key = int(key)
        values.append(key)

    return (values)


array = dict(zip(modulo(keys), keys))
print(array)
 
if __name__ == '__main__':

    def hash(self, key):
        """Get the index of our array for a specific string key"""
        length = len(self.array)
        return hash(key) % length
        
    def add(self, key, value):
        """Add a value to our array by its key"""
        index = self.hash(key)
        if self.array[index] is not None:
            # This index already contain some values.
            # This means that this add MIGHT be an update
            # to a key that already exist. Instead of just storing
            # the value we have to first look if the key exist.
            for kvp in self.array[index]:
                # If key is found, then update
                # its current value to the new value.
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                # If no breaks was hit in the for loop, it 
                # means that no existing key was found, 
                # so we can simply just add it to the end.
                self.array[index].append([key, value])
        else:
            # This index is empty. We should initiate 
            # a list and append our key-value-pair to it.
            self.array[index] = []
            self.array[index].append([key, value])

    def get(self, key):
        """Get a value by key"""
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            # Loop through all key-value-pairs
            # and find if our key exist. If it does
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            
            # If no return was done during loop,
            # it means key didn't exist.
            raise KeyError()
    hash
    add