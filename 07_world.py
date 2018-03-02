class World(object):

    def __init__(self):
        # creating world
        self.width = 100
        self.height = 200

        # list of object in world
        self.objects_in_world = []

    def check_if_there_are_collision_of_objects(self):
        for index, object in enumerate(self.objects_in_world):
            for collide_object in self.objects_in_world[index+1:]:
                # if object.position == colide_object.position:
                #     return True
                return object.collide(collide_object)



