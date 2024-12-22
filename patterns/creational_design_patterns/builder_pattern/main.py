from house import HouseBuilder


if __name__ == "__main__":
    one_bhk_house = HouseBuilder().add_walls(10).add_roof(1).add_windows(2).add_room(1).add_doors(10).build()
    two_bhk_house = HouseBuilder().add_walls(10).add_roof(1).add_windows(6).add_room(2).add_doors(10).build()
    print(one_bhk_house)
    print(two_bhk_house)