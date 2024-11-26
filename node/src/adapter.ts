interface IDuck {
  quack(): void;
  fly(): void;
}

class Duck implements IDuck {
  constructor() { }
  quack(): void {
    console.log("duck quack");
  }
  fly(): void {
    console.log("duck fly");
  }
}

interface ITurkey {
  gobble(): void;
  fly(): void
}

class Turkey implements ITurkey {
  constructor() { }
  gobble(): void {
    console.log("olokolokolok");
  }
  fly(): void {
    console.log("turkey flip flap");
  }
};


class TurkeyAdapter implements IDuck {
  turkey!: ITurkey;

  constructor(turkey: ITurkey) {
    this.turkey = turkey
  }

  fly(): void {
    this.turkey.fly();
  }

  quack(): void {
    this.turkey.gobble();
  }
}

const turkey = new Turkey();
const turkeyAdapter = new TurkeyAdapter(turkey);
const duck = new Duck();
const ducks: IDuck[] = [duck, turkeyAdapter];

function AdapterPattern() {
  for (const x of ducks) {
    x.quack();
    x.fly();
  }
}

export default AdapterPattern;
