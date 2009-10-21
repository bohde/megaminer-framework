import structures

client = 0
server = 1

UnitType = structures.Model('UnitType', key='objectID',
  data = ( ('objectID', int),
    ('name', str),
    ('price', int),
    ('hunger', int),
    ('traintime', int),
    ('hp', int),
    ('armor', int),
    ('moves', int),
    ('actions', int),
    ('attackcost', int),
    ('damage', int),
    ('minrange', int),
    ('maxrange', int),
    ('trainerID', int),
    ('canpaint', int))
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
    ('spawnY', int))
  )

Unit = structures.Model('Unit', key='objectID',
  data = ( ('objectID', int),
    ('x', int),
    ('y', int),
    ('z', int),
    ('hp', int),
    ('level', int),
    ('unitTypeID', int),
    ('ownerIndex', int),
    ('actions', int),
    ('moves', int)),
  functions = ( ('attack', ( ('x', int), ('y', int) ) ),
    ('build', ( ('x', int), ('y', int), ('type', BuildingType) ) ),
    ('paint', ( ('x', int), ('y', int)) ),
    ('move', ( ('x', int), ('y', int)) ),
    ('warp', () ) )
  )


Building = structures.Model('Building', key='objectID',
  data = ( ('objectID', int),
    ('x', int),
    ('y', int),
    ('z', int),
    ('hp', int),
    ('level', int),
    ('buildingTypeID', int),
    ('inTraining', int),
    ('progress', int),
    ('linked', int),
    ('complete', int)),
  functions = ( ('train', ( ('unit', UnitType), ) ),
    ('cancel', () ) )
  )

Terrain = structures.Model('Terrain', key='objectID',
  data = ( ('objectID', int),
    ('x', int),
    ('y', int),
    ('z', int),
    ('blockmove', int),
    ('blockbuild', int))
  )

Portal = structures.Model('Portal', key='objectID',
  data = ( ('objectID', int),
    ('x', int),
    ('y', int),
    ('z', int),
    ('direction', int),
    ('fee', int))
  )

turnNumber = structures.Global('turnNumber', int)
player0Gold0 = structures.Global('player0Gold0', int)
player0Gold1 = structures.Global('player0Gold1', int)
player0Gold2 = structures.Global('player0Gold2', int)
player1Gold0 = structures.Global('player1Gold0', int)
player1Gold1 = structures.Global('player1Gold1', int)
player1Gold2 = structures.Global('player1Gold2', int)
