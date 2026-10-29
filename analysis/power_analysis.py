from math import ceil

from statsmodels.stats.power import FTestAnovaPower, TTestIndPower


# ---------------------------------------------------------
# Study design assumptions
# ---------------------------------------------------------

ALPHA = 0.05
POWER = 0.80
N_GROUPS = 5

PRIMARY_EFFECT_SIZE_F = 0.20
RECRUITMENT_TARGET = 360


# ---------------------------------------------------------
# One-way ANOVA power analysis
# ---------------------------------------------------------

anova_power = FTestAnovaPower()

required_n = anova_power.solve_power(
    effect_size=PRIMARY_EFFECT_SIZE_F,
    k_groups=N_GROUPS,
    alpha=ALPHA,
    power=POWER,
)

required_n_rounded = ceil(required_n)

# Balanced sample across five conditions
balanced_n = ceil(required_n_rounded / N_GROUPS) * N_GROUPS
participants_per_condition = balanced_n // N_GROUPS


print("PRIMARY POWER ANALYSIS")
print("----------------------")
print(f"Test: One-way ANOVA")
print(f"Number of groups: {N_GROUPS}")
print(f"Alpha: {ALPHA}")
print(f"Power: {POWER}")
print(f"Cohen's f: {PRIMARY_EFFECT_SIZE_F}")
print(f"Estimated required N: {required_n:.2f}")
print(f"Rounded required N: {required_n_rounded}")
print(f"Balanced analyzable target: {balanced_n}")
print(f"Participants per condition: {participants_per_condition}")
print()


# ---------------------------------------------------------
# Effect-size sensitivity analysis
# ---------------------------------------------------------

effect_sizes = [0.15, 0.20, 0.25, 0.30]

print("EFFECT-SIZE SENSITIVITY")
print("-----------------------")

for effect_size in effect_sizes:
    n = anova_power.solve_power(
        effect_size=effect_size,
        k_groups=N_GROUPS,
        alpha=ALPHA,
        power=POWER,
    )

    print(
        f"Cohen's f = {effect_size:.2f} "
        f"-> estimated N = {n:.2f}, rounded N = {ceil(n)}"
    )

print()


# ---------------------------------------------------------
# Recruitment target
# ---------------------------------------------------------

recruitment_per_condition = RECRUITMENT_TARGET // N_GROUPS

print("RECRUITMENT TARGET")
print("------------------")
print(f"Total recruitment target: {RECRUITMENT_TARGET}")
print(f"Approximate participants per condition: {recruitment_per_condition}")
print()


# ---------------------------------------------------------
# Pairwise planned-contrast sensitivity
# ---------------------------------------------------------

ttest_power = TTestIndPower()

target_d = 0.47

required_per_group_d47 = ttest_power.solve_power(
    effect_size=target_d,
    alpha=ALPHA,
    power=POWER,
    ratio=1.0,
    alternative="two-sided",
)

required_per_group_d40 = ttest_power.solve_power(
    effect_size=0.40,
    alpha=ALPHA,
    power=POWER,
    ratio=1.0,
    alternative="two-sided",
)

print("PAIRWISE COMPARISON SENSITIVITY")
print("-------------------------------")
print(
    f"For Cohen's d = 0.47, approximately "
    f"{ceil(required_per_group_d47)} participants per group are required."
)
print(
    f"For Cohen's d = 0.40, approximately "
    f"{ceil(required_per_group_d40)} participants per group are required."
)
print()


# ---------------------------------------------------------
# Notes
# ---------------------------------------------------------

print("NOTES")
print("-----")
print(
    "The assumed effect size f = 0.20 is a design-stage planning "
    "assumption, not an empirical estimate from this study."
)
print(
    "This calculation primarily addresses the omnibus five-group ANOVA "
    "and does not establish adequate power for every proposed mediation "
    "or indirect effect."
)
