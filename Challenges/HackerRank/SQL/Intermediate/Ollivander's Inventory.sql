SELECT W.ID, WP.AGE, W.COINS_NEEDED, W.POWER 
FROM WANDS AS W
JOIN WANDS_PROPERTY AS WP
ON WP.CODE = W.CODE
WHERE WP.IS_EVIL = 0 AND W.COINS_NEEDED = (SELECT MIN(COINS_NEEDED) FROM WANDS JOIN WANDS_PROPERTY ON WANDS.CODE = WANDS_PROPERTY.CODE WHERE W.POWER = WANDS.POWER AND Wands_Property.age = WP.age)
ORDER BY W.POWER DESC, WP.AGE DESC;