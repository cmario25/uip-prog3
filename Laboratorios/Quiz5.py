#Laboratorios/quiz5.py

import unittest


class registro:

    try:

        def registro(self,usuario,edad):

            usuario=input("escribe tu nombre")

            edad=input("escribe tu edad")

            return {"usuario:":usuario,"apellido":usuario+"martinez","edad:":edad}

    except Exception:

        print("ERROR")


class NotificationsTestCase(unittest.TestCase):

    try:


        def test_user_repository(self):

            users=registro()

            user=users.registro("mario","22")


            self.assertEquals("mariomartinez",user['apellido'])

    except Exception:

        print("ERROR")


if __name__ == '__main__':

        unittest.main()
