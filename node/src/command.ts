/**
 * This file contains all the things related to command.ts and nothing else;
 * 
 *
 * What I have learned from the Head first design patters:
 *
 * Command pattern has:
 * Invoker - the client or the user that uses a common interface to execute commands
 * Set of side effects - a side effect does one action only e.g. turn on faucent, close garage, close door, lock door
 * Commands - implements a common interface thhat is used by the invoker
 *      - encapsulates a set of side effects in a method in which the method follows the rules of the interface
 *
 *
 * When to use?
 * Request response model
 * where in the requester does not need to know the specific implementation of how to fulfill its request
 * Where in the responders actions need to be encapsulated
 * where in each command contain a series of actions, 
 * ...and each command should be pluggable 
 * ...i.e. the client can choose to replace a command with the other command without having to change the code
 *
 *
 * 
 */


interface Command {
  execute(): void
}

class ACDevice {
  constructor() { }
  high() {
    console.log("ac is now high");
  }
  off() {
    console.log("ac is now off");
  }
  on() {
    console.log("ac is now on");
  }
}

class MacroCommand implements Command {
  commands: Command[] = [];

  constructor() {

  }

  setCommands(commands: Command[]) {
    this.commands = commands;
  }

  execute() {
    for (const c of this.commands) {
      c.execute();
    }
  };
}

class ACDeviceOnCommand {
  ac_device: ACDevice | null = null;

  constructor(ac_device: ACDevice) {
    if (this.ac_device == null) {
      this.ac_device = ac_device;
    }
  }

  execute() {
    if (this.ac_device != null) {
      this.ac_device.on();
      this.ac_device.high();
    }
  }
}

class ACDeviceOffCommand {

  ac_device: ACDevice | null = null;

  constructor(ac_device: ACDevice) {
    if (this.ac_device == null) {
      this.ac_device = ac_device;
    }
  }

  execute() {
    if (this.ac_device != null) {
      this.ac_device.off();
    }
  }
}

class NoCommand {
  constructor() { }
  execute() { }
}

class RemoteDevice {
  buttons: Command[] = [];
  constructor(numberOfButtons: number) {
    for (let i = 0; i < numberOfButtons; i++) {
      this.buttons.push(new NoCommand());
    }
  }

  setCommand(buttonSlot: number, command: Command) {
    const isValidSlot = buttonSlot < this.buttons.length && buttonSlot >= 0;
    if (!isValidSlot) {
      return
    }
    this.buttons[buttonSlot] = command;
  }

  press(buttonSlot: number) {
    const isValidSlot = buttonSlot < this.buttons.length && buttonSlot >= 0;
    if (!isValidSlot) {
      return
    }
    this.buttons[buttonSlot].execute();
  }
}



function CommandPattern() {

  const remote = new RemoteDevice(2);
  const acDevice = new ACDevice();
  const acOn = new ACDeviceOnCommand(acDevice);
  const acOff = new ACDeviceOffCommand(acDevice);

  remote.setCommand(0, acOn);
  remote.setCommand(1, acOff);
  remote.press(0);
  remote.press(1);
}
export default CommandPattern;

