# Contested Garment Rule

The Contested Garment Rule splits a supply across claimants in a "fair" way. This algorithm can be applied to The Bankruptcy Problem, where a person dies and their estate is to be split fairly across claimants.

https://en.wikipedia.org/wiki/Contested_garment_rule

https://www.youtube.com/watch?v=uNemXgZ-MWY

## How does it work?

It's different to something like proportional splitting as it considers parts of claims that are contested and uncontested differently.

For example, if claimant 1 claims less than claimant 2, the contested garment rule assumes the part not claimed by claimant 1 is "uncontested", and this uncontested amount is given straight to  claimant 2. The "contested" amount is then split evenly.

E.g. `Supply=100, claimants=[50,80]`. A total of 30 is uncontested by claimant 1 and this will first be awarded to claimant 2, and the remainder (70) should be split equally between the parties.

```
Output contested garment rule = [35,65]
Output proportional = [38.5,61.5]
```

## Why use this over more simple fairness rules?

The rule offers a different idea of what it is to be fair. Some people may consider this to be more fair than proportional splitting. The justification for this is the contested garment rule aims to ensure everyone "gains" an equal amount when the supply is dwarfed by the total claims. For bigger supplies, it tries to ensure everyone "loses" an equal amount.

The result of this is that (compared to proportional splitting), the contested garment rule will favour small claimants when the supply amounts to less than half of the total claims amount, and will favour big claimants when the supply amounts to more than half of the total claims amount.

Overall, I can't think of a situation where you would use this over a proportional split. 

My opinion is:

1. It's less fair than proportional splitting (see examples)
2. It can be gamed by splitting your claim across multiple entities, whereas this would not work in a proportional split. (see examples) 
3. It's harder to explain and reason about. There has to be considerable benefit to counter the additional complexity, which for the use cases I'm working with I cannot see.

## What is used in the real world?

In a real life bankrupty problem where a business is made insolvent, the supply is shared first by priority, with higher priority claimants receiving their claims first. When there is not enough to share to all claimants in a priority tier, the supply is shared "pro-rata", or proportionally within the tier.

https://www.investopedia.com/ask/answers/09/corporate-liquidation-unpaid-taxes-wages.asp

## Examples
### Favouring small claimants on small supply

Here, claimant 1 (small) is awarded 50% of their claim, while claimant 2 (large) is awarded 2% of their claim.

```
Supply=5
Claimants=[5,125]
Output contested garment rule = [2.5,2.5]
Output proportional = [0.19,4.81]
```

### Favouring big claimants on larger supply

In this example, claimant 1 (small) is still awarded 50% of their claim, while claimant 2 (large) is awarded 98% of their claim.

```
Supply=125
Claimants=[5,125]
Output contested garment rule = [2.5,122.5]
Output proportional = [4.81,120.19]
```

### Gaming the system by splitting your claim across multiple entities

This takes from the 1st example, but instead has the larger claimant split their claim across many different claimants. You can imagine a real life example of this being a single company making a claim vs the individual shareholders making a claim. By doing this, the second claimant gets awarded far more of the supply than if they'd just made the claim as a single entity. Note, this only applies when the supply is less than half of the total demand. If the supply is more than half the demand, they'd be better off making the claim as a single entity.

In the original example where claimant 2 made their claim under a single entity, claimant 1 was favoured, with claimant 1 awarded 50% of their claim, while claimant 2 was awarded 2% of their claim. Now, when claimant 2 splits their claim, claimant 1 is now only awarded 0.8% of their claim, while claimant 2 is awarded 3.97% of their claim.

```
Supply=5
Claimants=[5,[1,1,1,1,1,1,1,...]]
Output contested garment rule = [0.04,[0.04,0.04,0.04,0.04,...]]  = [0.04,4.96]
Output proportional = [0.19,4.81]
```