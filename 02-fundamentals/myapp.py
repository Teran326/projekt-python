import physics

if(physics.egikphs(physics.EARTH_GRAVITY) > physics.mgikphs(physics.MOON_GRAVITY)):
    print("Země má větší gravitační zrychlení než měsíc")
else:
    print("Měsíc má větší gravitační zrychlení než Země")
if(physics.solikph(physics.SPEED_OF_LIGHT) < physics.sosikph(physics.SPEED_OF_LIGHT)):
    print("Rychlost zvuku je větší než rychost světla")
else:
    print("Rychlost světla je větší než rychost zvuku")