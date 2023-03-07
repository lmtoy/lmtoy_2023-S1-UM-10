# 2023-S1-UM-10


## Min's first comments:

There are a few chassis-board combinations that are consistently
unreliable, and I request the follow C-B combinations flagged for all
observations: 0-2, 1-1, 1-2, 2-1, 2-4, 3-3, 3-4, and 3-5.  Some of
these are working "OK" (e.g., 0-2, 1-2), but they consistently produce
artifacts.

There are also some C-B combinations that are intermittently poor.  I
list the affected integrations for the specific C-Bs:

     0-0: 104701, 104744, 194745
     1-0: 104704, 104705, 104744, 104745, 104748, 104749, 104750, 104754, 104871, 104880, 
     2-0: 104449-104455, 104540-104546, 104865-104871, 
     3-2: 104540-104546, 104883-104889

Note that J164229.74+554957.0 (ObsNums 104883-104889) has only one good chassis covering board 2 and should be repeated.

badcb=0/2,1/1,1/2,2/1,2/4,3/3,3/4,3/5


## Peter's comments

1/1,2/1,2/4,3/5 are jittery in tsys    (1/0 usually recovers after badlags)
3/3 sometimes added
