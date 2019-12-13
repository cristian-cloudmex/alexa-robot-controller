"""
Logic between the Raspberry Pi and the LED light. Changes maintained through
the Light object and the pigpio daemon connection.
"""
import time
import logging
import pigpio

# Logger information
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

class RobotMoves(object):
    """
    Light object to maintian logic of the state of the lights and
    Gpio ports
    """
    def __init__(self):
        super(RobotMoves, self).__init__()
        self.movimiento = 'parar'
        # Establish connection to pigpio daemon
        self.pi = pigpio.pi()

    def current_setting(self):
        """
        Gives current settings of Light object.

        Returns:
            Python dict of Light object power state and brightness
        """
        return {
                   'movimiento': self.movimiento
               }

    def needs_updating(self, robot_data):
        """
        Determines if Light object needs to update its settings based on new
        light data.

        Args:
            light_data: Python dict of new light data to represent
        Returns:
            boolean
        """
        if robot_data.get('movimiento') != self.movimiento:
            return True
        return False

    def update_robot_data(self, robot_data):
        """
        Updates Light object needs to update its settings. Sets
        current brightness to old brightness setting before updating brightness
        and power_state. Will update brightness and current brightness even
        if in off state.

        Args:
            light_data: Python dict of new light data to represent
        Returns:
            boolean
        """
        self.movimiento = robot_data.get('movimiento')
        self._update_board()

    def _update_board(self):
        """
        Updates light brightness if power state is on. Otherwise sets the
        lights to OFF color. Logs current settings after updating.

        Args:
            None
        """

        if self.movimiento.lower() == "adelante":
            pass
        elif self.movimiento.lower() == "atras":
            pass
        elif self.movimiento.lower() == "derecha":
            pass
        elif self.movimiento.lower() == "izquierda":
            pass
        elif self.movimiento.lower() == "parar":
            pass        
        logger.info(self.movimiento)

    
