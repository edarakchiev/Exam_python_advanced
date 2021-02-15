from collections import deque

firework_effects = deque([int(num) for num in input().split(', ') if int(num) > 0])
explosion_power = [int(n) for n in input().split(', ') if int(n) > 0]

palm = 0
willow = 0
crossette = 0

is_prepared = False
while firework_effects and explosion_power:
    effect = firework_effects.popleft()
    power = explosion_power[-1]
    current_sum = effect + power

    if current_sum % 3 == 0 and not current_sum % 5 == 0:
        palm += 1
        explosion_power.pop()
    elif not current_sum % 3 == 0 and current_sum % 5 == 0:
        willow += 1
        explosion_power.pop()
    elif current_sum % 3 == 0 and current_sum % 5 == 0:
        crossette += 1
        explosion_power.pop()
    else:
        effect -= 1
        if effect > 0:
            firework_effects.append(effect)
    if palm >= 3 and willow >= 3 and crossette >= 3:
        is_prepared = True
        break


if is_prepared:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")
if firework_effects:
    firework_effects = [str(e) for e in firework_effects]
    print(f"Firework Effects left: {', '.join(firework_effects) }")
if explosion_power:
    explosion_power = [str(p) for p in explosion_power]
    print(f"Explosive Power left: {', '.join(explosion_power)}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")
