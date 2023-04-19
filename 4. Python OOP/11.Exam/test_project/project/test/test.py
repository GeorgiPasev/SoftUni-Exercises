from project.robot import Robot
import unittest


class TestRobot(unittest.TestCase):

    def setUp(self):
        self.robot = Robot("R1", "Military", 100, 5000)

    def test_init(self):
        self.assertEqual(self.robot.robot_id, "R1")
        self.assertEqual(self.robot.category, "Military")
        self.assertEqual(self.robot.available_capacity, 100)
        self.assertEqual(self.robot.price, 5000)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])

    def test_category_setter(self):
        self.robot.category = "Education"
        self.assertEqual(self.robot.category, "Education")
        
        with self.assertRaises(ValueError) as ex:
            self.robot.category = "Medical"
        self.assertEqual(str(ex.exception), "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_price_setter(self):
        self.robot.price = 6000
        self.assertEqual(self.robot.price, 6000)

        with self.assertRaises(ValueError) as ex:
            self.robot.price = -1000
        self.assertEqual(str(ex.exception), "Price cannot be negative!")

    def test_upgrade(self):
        result = self.robot.upgrade("Laser", 1000)
        self.assertEqual(result, "Robot R1 was upgraded with Laser.")
        self.assertEqual(self.robot.hardware_upgrades, ["Laser"])
        self.assertEqual(self.robot.price, 6500)

        result = self.robot.upgrade("Laser", 1000)
        self.assertEqual(result, "Robot R1 was not upgraded.")
        self.assertEqual(self.robot.hardware_upgrades, ["Laser"])
        self.assertEqual(self.robot.price, 6500)

    def test_update(self):
        result = self.robot.update(1.1, 50)
        self.assertEqual(result, "Robot R1 was updated to version 1.1.")
        self.assertEqual(self.robot.software_updates, [1.1])
        self.assertEqual(self.robot.available_capacity, 50)

        result = self.robot.update(1.0, 10)
        self.assertEqual(result, "Robot R1 was not updated.")
        self.assertEqual(self.robot.software_updates, [1.1])
        self.assertEqual(self.robot.available_capacity, 50)

        result = self.robot.update(1.2, 60)
        self.assertEqual(result, "Robot R1 was not updated.")
        self.assertEqual(self.robot.software_updates, [1.1])
        self.assertEqual(self.robot.available_capacity, 50)

    def test_gt(self):
        other_robot = Robot("R2", "Education", 50, 3000)
        self.assertTrue(self.robot > other_robot)
        self.assertFalse(other_robot > self.robot)
        other_robot.price = 5000
        self.assertFalse(self.robot > other_robot)
        self.assertFalse(other_robot > self.robot)



if __name__ == "__main__":
    unittest.main()