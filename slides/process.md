## **Spin Coating (step_1)**

```
start
  |
  |---> Pipette Preparation:
  |         Pipette Rack Number
  |         Tip Type
  |         Solution Number
  |         Solution Volume (uL)
  |         Solvent Station Number
  |
  |---> (optional) Mixing:
  |         Mixing Cycles Aspiration (0-9)
  |         Liquid Class Index Aspiration
  |         Liquid Class Index Dispensing
  |
  |---> Dispense onto substrate:
  |         Pipette Dispensing Height Above Substrate (mm)
  |
  |---> Wait:
  |         Dispense-Spin/Blade Delay (s)
  |
  |---> Spin:
  |         Spin Acceleration (rpm/s)
  |         Spin Time (s)
  |         Spin Velocity (rpm)
  |         Spincoater Number
  |
  |---> (optional) Put on Hotplate:
  |         Put on Hotplate
  |
  |---> (optional) Annealing:
  |         Annealing Station Number
  |         Annealing Temperature (°C)
  |         Annealing Time (s)
  |
  |---> Discard Pipettes
```

---

## **Whirl Spin Coating (step_2)**

```
start
  |
  |---> Pipette Preparation:
  |         Pipette Rack Number
  |         Tip Type
  |         Solution Number
  |         Solution Volume (uL)
  |         Solvent Station Number
  |
  |---> (optional) Mixing:
  |         Mixing Cycles Aspiration (0-9)
  |         Liquid Class Index Aspiration
  |         Liquid Class Index Dispensing
  |
  |---> Set Spincoater to Initial Spin Velocity:
  |         Initial Spin Velocity (Before Dispensing) (rpm)
  |
  |---> Move Arm at Speed and Dispense along Range:
  |         Arm Speed While Dispending (0-100%)
  |         Dispense range (mm)
  |         Pipette Dispensing Height Above Substrate (mm)
  |
  |---> Wait:
  |         Dispense-Spin/Blade Delay (s)
  |
  |---> Spin (main spin):
  |         Spin Acceleration (rpm/s)
  |         Spin Time (s)
  |         Spin Velocity (rpm)
  |         Spincoater Number
  |
  |---> (optional) Put on Hotplate:
  |         Put on Hotplate
  |
  |---> (optional) Annealing:
  |         Annealing Station Number
  |         Annealing Temperature (°C)
  |         Annealing Time (s)
  |
  |---> Discard Pipettes
```

---

## **Pipette Quenching (step_3)**

```
start
  |
  |---> Pipette Preparation:
  |         Pipette Rack Number
  |         Tip Type
  |         Solution Number
  |         Solution Volume (uL)
  |         Solvent Station Number
  |
  |---> (optional) Mixing:
  |         Mixing Cycles Aspiration (0-9)
  |         Liquid Class Index Aspiration
  |         Liquid Class Index Dispensing
  |
  |---> Dispense onto substrate:
  |         Pipette Dispensing Height Above Substrate (mm)
  |
  |---> Wait:
  |         Dispense-Spin/Blade Delay (s)
  |
  |---> Spin:
  |         Spin Acceleration (rpm/s)
  |         Spin Time (s)
  |         Spin Velocity (rpm)
  |         Spincoater Number
  |
  |---> Quench Step:
  |         Quench Pipette Rack Number
  |         Quench Tip Type
  |         Quench Solution Number
  |         Quench Solution Volume (uL)
  |         Quench Solvent Station Number
  |         Quench Height Above Substrate (mm)
  |         Quench Liquid Class Index Aspiration
  |         Quench Liquid Class Index Dispensing
  |
  |---> Wait:
  |         Quench-Spin Delay (s)
  |
  |---> Second Spin:
  |         Second Spin Acceleration (rpm/s)
  |         Second Spin Time (s)
  |         Second Spin Velocity (rpm)
  |
  |---> (optional) Put on Hotplate:
  |         Put on Hotplate
  |
  |---> (optional) Annealing:
  |         Annealing Station Number
  |         Annealing Temperature (°C)
  |         Annealing Time (s)
  |
  |---> Discard Pipettes
  |
  |---> (optional) Decap and Recap Vial
```

---

## **Solvent Mixing (step_4)**

```
start
  |
  |---> Aspirate:
  |         Aspirate Index
  |         Aspirate Solution Number
  |         Aspirate Solvent Station Number
  |         Aspirate Volume
  |
  |---> Dispense:
  |         Dispense Index
  |         Dispense Solution Number
  |         Dispense Solvent Station Number
  |         Dispense Volume
  |
  |---> (optional) Load Dispense Matrix
  |
  |---> Pipette Preparation:
  |         Pipette Rack Number
  |         Tip Type
  |
  |---> Discard Pipettes
```

---

## **Take Photo (step_5 & step_6)**

```
start
  |
  |---> Take Photo: true
```

---

**All parameters are now included and in the correct order for each process.**