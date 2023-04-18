from unittest import TestCase, main
from project.toy_store import ToyStore

class TestToyStore(TestCase()):

    def setUp(self):
        self.toy_store = ToyStore()
    
    def test_correct__innit(self):
        for key in range(ord("A"), ord("G") + 1):
            self.assertIsNone(self.store.toy_shelf[chr(key)])
        
        self.assertEqual(7, len(self.store.toy_shelf))

    def test_add_toy_on_non_existing_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("H", "Toy")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_that_is_already_on_shelf_raises_exception(self):
        self.store.add_toy("A", "Toy")

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Toy")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))
        
    def test_add_toy_to_a_full_shelf_raises_exception(self):
        self.store.add_toy("A", "Doll")

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Toy")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_successfully_returns_string(self):
        result = self.store.add_toy("A", "Doll")

        self.assertEqual("Toy:Doll placed successfully!", result)
        self.assertEqual("Doll", self.store.toy_shelf["A"])
    
    def test_remove_toy_from_non_existing_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("H", "Toy")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
    
    def test_remove_non_existing_toy_from_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "Toy")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))
        
    def test_remove_toy_corretly_returns_string(self):
        self.store.toy_shelf["A"] = "Doll"

        result = self.store.remove_toy("A", "Doll")

        self.assertIsNone(self.store.toy_shelf["A"])
        self.assertEqual("Remove toy:Doll successfully!", result)


if __name__ == "__main__":
    main()

