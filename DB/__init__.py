import DB.controller


DBS = controller.Controller()


def run_server():
    ds = DBS.get_user_by_email('30005819@students.ual.pt')
    print(ds)

