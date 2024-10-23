class State:
    START = "Start"
    PROCESS = "Process"
    FINISH = "Finish"


class StateMachine:
    def __init__(self) -> None:
        self.state = State.START

    def transition(self):
        if self.state == State.START:
            print("transition to process")
            self.state = State.PROCESS

        elif self.state == State.PROCESS:
            print("transition to Finish")
            self.state = State.FINISH

        else:
            print("Alread in Finish")

    def curr_state(self):
        return self.state


if __name__ == "__main__":
    sm = StateMachine()
    print(f"Current state: {sm.curr_state()}")
    sm.transition()
    print(f"Current state: {sm.curr_state()}")
    sm.transition()
    print(f"Current state: {sm.curr_state()}")
