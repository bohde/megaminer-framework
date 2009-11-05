import structures

client = 0
server = 1

UnitType = structures.Model('UnitType', key='objectID',
  data = ( ('objectID', int),
    ('name', str),
    ('price', int),
    ('hunger', int),
    ('trainTime', int),
    ('hp', int),
    ('armor', int),
    ('moves', int),
    ('actions', int),
    ('attackCost', int),
    ('damage', int),
    ('minRange', int),
    ('maxRange', int),
    ('trainerID', int),
    ('canPaint', int),
    ('armorExp', float),
    ('hpExp', float),
    ('priceExp', float),
    ('damageExp', float),
    ('paintBase', int),
    ('paintLinear', int)),
  doc = 'This defines the attributes of a kind of unit.'
  )

BuildingType = structures.Model('BuildingType', key='objectID',
  data = ( ('objectID', int),
    ('name', str),
    ('price', int),
    ('food', int),
    ('pastBuildTime', int),
    ('presentBuildTime', int),
    ('futureBuildTime', int),
    ('hp', int),
    ('armor', int),
    ('builderID', int),
    ('allowPaint', int),
    ('width', int),
    ('height', int),
    ('spawnX', int),
    ('spawnY', int),
    ('armorExp', float),
    ('hpExp', float),
    ('priceExp', float),
    ('foodExp', float)),
  doc = 'This defines the attributes of a kind of building.'
  )

Unit = structures.Model('Unit', key='objectID',
  data = ( ('objectID', int),
    ('x', int),
    ('y', int),
    ('z', int),
    ('hp', int),
    ('level', int),
    ('unitTypeID', int),
    ('ownerID', int),
    ('actions', int),
    ('moves', int)),
  functions = ( ('attack', ( ('x', int), ('y', int) ) ),
    ('build', ( ('x', int), ('y', int), ('type', BuildingType) ) ),
    ('paint', ( ('x', int), ('y', int)) ),
    ('move', ( ('x', int), ('y', int)) ),
    ('warp', () ) ),
  doc = 'An entitiy that can move around the game and act.'
  )


Building = structures.Model('Building', key='objectID',
  data = ( ('objectID', int),
    ('x', int),
    ('y', int),
    ('z', int),
    ('hp', int),
    ('level', int),
    ('buildingTypeID', int),
    ('ownerID', int),
    ('inTraining', int),
    ('progress', int),
    ('linked', int),
    ('complete', int)),
  functions = ( ('train', ( ('unit', UnitType), ) ),
    ('cancel', () ) ),
  doc = 'A building to shelter, feed, and/or create units.'
  )

Terrain = structures.Model('Terrain', key='objectID',
  data = ( ('objectID', int),
    ('x', int),
    ('y', int),
    ('z', int),
    ('blocksMove', int),
    ('blocksBuild', int)),
  doc = 'The attributes of a specific tile of the world.'
  )

Portal = structures.Model('Portal', key='objectID',
  data = ( ('objectID', int),
    ('x', int),
    ('y', int),
    ('z', int),
    ('direction', int),
    ('fee', int),
    ('feeIncr', int),
    ('feeMultiplier', float)),
  doc = 'A connection between two adjacent times.'
  )

turnNumber = structures.Global('turnNumber', int)
player0Gold0 = structures.Global('player0Gold0', int, 'Player 0\'s past gold')
player0Gold1 = structures.Global('player0Gold1', int, 'Player 0\'s present gold')
player0Gold2 = structures.Global('player0Gold2', int, 'Player 0\'s future gold')
player1Gold0 = structures.Global('player1Gold0', int, 'Player 1\'s past gold')
player1Gold1 = structures.Global('player1Gold1', int, 'Player 1\'s present gold')
player1Gold2 = structures.Global('player1Gold2', int, 'Player 1\'s future gold')
playerID = structures.Global('playerID', int, 'Player Number; either 0 or 2')
maxX = structures.Global('maxX', int)
maxY = structures.Global('maxY', int)

