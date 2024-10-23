from multiprocessing import Process, Pipe
import time


def sender_task(conn):
    for idx in range(5):
        message = f"Message {idx} from Sender process"
        conn.send(message)
        print(f"Message sent: {message}")
        time.sleep(1)
    conn.send("STOP")
    conn.close()


def recver_task(conn):
    while True:
        reciept = conn.recv()
        if reciept == "STOP":
            break
        print("Recieved Process: {reciept}")
    conn.close()


if __name__ == "__main__":
    sender, recievr = Pipe()
    # the sender reciever is similar to the tx, rx in mspc
    # that is used in between threads in rust
    p1 = Process(target=sender_task, args=(sender,))
    p2 = Process(target=recver_task, args=(recievr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Completed processes")
