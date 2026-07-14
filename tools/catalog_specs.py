"""Curated specifications for all standalone applications."""

from __future__ import annotations

from tools.catalog_models import (
    AppSpec,
    FileApp,
    FormulaApp,
    GameApp,
    GeneratorApp,
    Parameter,
    QuizApp,
    TextApp,
)


def p(name: str, default: float, help_text: str) -> Parameter:
    """Build numeric parameter."""
    return Parameter(name, default, help_text)


def formula(
    category: str,
    slug: str,
    title: str,
    summary: str,
    parameters: tuple[Parameter, ...],
    outputs: tuple[tuple[str, str], ...],
    validations: tuple[tuple[str, str], ...] = (),
) -> FormulaApp:
    """Build formula app specification."""
    return FormulaApp(
        category,
        slug,
        title,
        summary,
        parameters,
        outputs,
        validations,
    )


CALCULATORS: tuple[AppSpec, ...] = (
    formula(
        "calculators",
        "tip_calculator",
        "Tip Calculator",
        "Split a restaurant bill with a configurable tip.",
        (
            p("subtotal", 64.0, "Bill before tip."),
            p("tip_percent", 20.0, "Tip percent."),
            p("people", 2.0, "People sharing bill."),
        ),
        (
            ("Tip", "subtotal * tip_percent / 100"),
            ("Total", "subtotal * (1 + tip_percent / 100)"),
            ("Per person", "subtotal * (1 + tip_percent / 100) / people"),
        ),
        (
            ("subtotal < 0", "subtotal cannot be negative"),
            ("people <= 0", "people must be positive"),
        ),
    ),
    formula(
        "calculators",
        "unit_price_comparator",
        "Unit Price Comparator",
        "Compare two package prices using cost per unit.",
        (
            p("price_a", 8.49, "First package price."),
            p("units_a", 24.0, "First package units."),
            p("price_b", 6.99, "Second package price."),
            p("units_b", 18.0, "Second package units."),
        ),
        (
            ("A per unit", "price_a / units_a"),
            ("B per unit", "price_b / units_b"),
            ("Difference", "abs(price_a / units_a - price_b / units_b)"),
        ),
        (("units_a <= 0 or units_b <= 0", "package units must be positive"),),
    ),
    formula(
        "calculators",
        "compound_interest",
        "Compound Interest Calculator",
        "Estimate investment growth with monthly compounding.",
        (
            p("principal", 5000.0, "Starting balance."),
            p("annual_rate", 6.0, "Annual percentage rate."),
            p("years", 10.0, "Years invested."),
        ),
        (
            ("Future value", "principal * (1 + annual_rate / 1200) ** (years * 12)"),
            (
                "Interest earned",
                "principal * (1 + annual_rate / 1200) ** (years * 12) - principal",
            ),
        ),
        (("principal < 0 or years < 0", "principal and years cannot be negative"),),
    ),
    formula(
        "calculators",
        "loan_payment",
        "Loan Payment Calculator",
        "Estimate monthly payment and total loan cost.",
        (
            p("principal", 20000.0, "Amount borrowed."),
            p("annual_rate", 7.0, "Annual percentage rate."),
            p("years", 5.0, "Loan duration in years."),
        ),
        (
            (
                "Monthly payment",
                "principal * (annual_rate / 1200) * (1 + annual_rate / 1200) ** (years * 12) / ((1 + annual_rate / 1200) ** (years * 12) - 1)",
            ),
            (
                "Total paid",
                "years * 12 * principal * (annual_rate / 1200) * (1 + annual_rate / 1200) ** (years * 12) / ((1 + annual_rate / 1200) ** (years * 12) - 1)",
            ),
        ),
        (
            (
                "principal <= 0 or annual_rate <= 0 or years <= 0",
                "all inputs must be positive",
            ),
        ),
    ),
    formula(
        "calculators",
        "bmi_calculator",
        "BMI Calculator",
        "Calculate body mass index from metric measurements.",
        (
            p("weight_kg", 72.0, "Weight in kilograms."),
            p("height_cm", 175.0, "Height in centimeters."),
        ),
        (("BMI", "weight_kg / (height_cm / 100) ** 2"),),
        (("weight_kg <= 0 or height_cm <= 0", "weight and height must be positive"),),
    ),
    formula(
        "calculators",
        "running_pace",
        "Running Pace Calculator",
        "Convert race distance and finish time into running pace.",
        (
            p("distance_km", 10.0, "Distance in kilometers."),
            p("minutes", 52.0, "Finish time in minutes."),
        ),
        (
            ("Minutes per kilometer", "minutes / distance_km"),
            ("Kilometers per hour", "distance_km / (minutes / 60)"),
        ),
        (("distance_km <= 0 or minutes <= 0", "distance and time must be positive"),),
    ),
    formula(
        "calculators",
        "fuel_cost",
        "Fuel Cost Calculator",
        "Estimate fuel volume and trip cost.",
        (
            p("distance_km", 450.0, "Trip distance."),
            p("liters_per_100km", 7.2, "Vehicle consumption."),
            p("price_per_liter", 1.65, "Fuel price."),
        ),
        (
            ("Liters", "distance_km * liters_per_100km / 100"),
            ("Trip cost", "distance_km * liters_per_100km / 100 * price_per_liter"),
        ),
        (
            (
                "distance_km < 0 or liters_per_100km < 0 or price_per_liter < 0",
                "inputs cannot be negative",
            ),
        ),
    ),
    formula(
        "calculators",
        "recipe_scaler",
        "Recipe Scaler",
        "Scale an ingredient amount between serving counts.",
        (
            p("amount", 2.5, "Original ingredient amount."),
            p("original_servings", 4.0, "Original servings."),
            p("new_servings", 7.0, "Desired servings."),
        ),
        (
            ("Scaled amount", "amount * new_servings / original_servings"),
            ("Scale factor", "new_servings / original_servings"),
        ),
        (("original_servings <= 0 or new_servings <= 0", "servings must be positive"),),
    ),
    formula(
        "calculators",
        "temperature_converter",
        "Temperature Converter",
        "Convert Celsius into Fahrenheit and Kelvin.",
        (p("celsius", 22.0, "Temperature in Celsius."),),
        (("Fahrenheit", "celsius * 9 / 5 + 32"), ("Kelvin", "celsius + 273.15")),
        (("celsius < -273.15", "temperature cannot be below absolute zero"),),
    ),
    formula(
        "calculators",
        "length_converter",
        "Length Converter",
        "Convert meters into common metric and imperial lengths.",
        (p("meters", 5.0, "Length in meters."),),
        (
            ("Centimeters", "meters * 100"),
            ("Feet", "meters * 3.28084"),
            ("Inches", "meters * 39.3701"),
        ),
    ),
    formula(
        "calculators",
        "data_size_converter",
        "Data Size Converter",
        "Convert bytes into binary storage units.",
        (p("byte_count", 1048576.0, "Number of bytes."),),
        (
            ("KiB", "byte_count / 1024"),
            ("MiB", "byte_count / 1024**2"),
            ("GiB", "byte_count / 1024**3"),
        ),
        (("byte_count < 0", "byte count cannot be negative"),),
    ),
    formula(
        "calculators",
        "age_in_days",
        "Age in Days Estimator",
        "Estimate age in days and hours from years.",
        (p("years", 25.0, "Age in years."),),
        (("Days", "years * 365.2425"), ("Hours", "years * 365.2425 * 24")),
        (("years < 0", "years cannot be negative"),),
    ),
    formula(
        "calculators",
        "grade_average",
        "Weighted Grade Calculator",
        "Combine two assessment scores using configurable weights.",
        (
            p("score_a", 88.0, "First score."),
            p("weight_a", 40.0, "First weight percent."),
            p("score_b", 94.0, "Second score."),
            p("weight_b", 60.0, "Second weight percent."),
        ),
        (
            (
                "Weighted grade",
                "(score_a * weight_a + score_b * weight_b) / (weight_a + weight_b)",
            ),
        ),
        (
            (
                "weight_a < 0 or weight_b < 0 or weight_a + weight_b <= 0",
                "weights must have a positive total",
            ),
        ),
    ),
    formula(
        "calculators",
        "break_even",
        "Break-even Calculator",
        "Find sales volume needed to cover fixed costs.",
        (
            p("fixed_cost", 12000.0, "Fixed costs."),
            p("price", 45.0, "Sale price per unit."),
            p("variable_cost", 18.0, "Variable cost per unit."),
        ),
        (
            ("Break-even units", "fixed_cost / (price - variable_cost)"),
            ("Contribution margin", "price - variable_cost"),
        ),
        (
            (
                "fixed_cost < 0 or price <= variable_cost",
                "price must exceed variable cost",
            ),
        ),
    ),
    formula(
        "calculators",
        "electricity_cost",
        "Electricity Cost Calculator",
        "Estimate appliance energy use and cost.",
        (
            p("watts", 900.0, "Appliance power."),
            p("hours_per_day", 2.0, "Daily use hours."),
            p("days", 30.0, "Days used."),
            p("price_per_kwh", 0.18, "Electricity price."),
        ),
        (
            ("Energy kWh", "watts / 1000 * hours_per_day * days"),
            ("Cost", "watts / 1000 * hours_per_day * days * price_per_kwh"),
        ),
        (
            (
                "watts < 0 or hours_per_day < 0 or days < 0 or price_per_kwh < 0",
                "inputs cannot be negative",
            ),
        ),
    ),
    formula(
        "calculators",
        "paint_estimator",
        "Paint Estimator",
        "Estimate paint needed for rectangular walls.",
        (
            p("wall_width", 4.5, "Wall width in meters."),
            p("wall_height", 2.4, "Wall height in meters."),
            p("walls", 4.0, "Number of walls."),
            p("coverage", 10.0, "Square meters per liter."),
            p("coats", 2.0, "Number of coats."),
        ),
        (
            ("Area", "wall_width * wall_height * walls"),
            ("Liters", "wall_width * wall_height * walls * coats / coverage"),
        ),
        (
            (
                "wall_width <= 0 or wall_height <= 0 or walls <= 0 or coverage <= 0 or coats <= 0",
                "all inputs must be positive",
            ),
        ),
    ),
    formula(
        "calculators",
        "time_zone_offset",
        "Time Zone Offset Calculator",
        "Shift a 24-hour clock time by a UTC offset.",
        (
            p("hour", 14.5, "Source decimal hour."),
            p("offset_hours", -7.0, "Hours to add."),
        ),
        (("Shifted hour", "(hour + offset_hours) % 24"),),
        (("hour < 0 or hour >= 24", "hour must be between 0 and 24"),),
    ),
    formula(
        "calculators",
        "percentage_change",
        "Percentage Change Calculator",
        "Measure absolute and percentage change between values.",
        (
            p("old_value", 80.0, "Starting value."),
            p("new_value", 92.0, "Ending value."),
        ),
        (
            ("Absolute change", "new_value - old_value"),
            ("Percentage change", "(new_value - old_value) / abs(old_value) * 100"),
        ),
        (("old_value == 0", "old value cannot be zero"),),
    ),
    formula(
        "calculators",
        "savings_goal",
        "Savings Goal Calculator",
        "Estimate months needed to reach a savings target.",
        (
            p("target", 10000.0, "Savings target."),
            p("current", 1500.0, "Current savings."),
            p("monthly", 450.0, "Monthly contribution."),
        ),
        (
            ("Amount remaining", "max(0, target - current)"),
            ("Months needed", "max(0, target - current) / monthly"),
        ),
        (
            (
                "target < 0 or current < 0 or monthly <= 0",
                "target and current cannot be negative; monthly must be positive",
            ),
        ),
    ),
    formula(
        "calculators",
        "screen_ppi",
        "Screen PPI Calculator",
        "Calculate display pixel density from resolution and diagonal size.",
        (
            p("width_px", 2560.0, "Horizontal pixels."),
            p("height_px", 1440.0, "Vertical pixels."),
            p("diagonal_inches", 27.0, "Screen diagonal."),
        ),
        (("Pixels per inch", "(width_px**2 + height_px**2) ** 0.5 / diagonal_inches"),),
        (
            (
                "width_px <= 0 or height_px <= 0 or diagonal_inches <= 0",
                "all inputs must be positive",
            ),
        ),
    ),
)


PLANNING: tuple[AppSpec, ...] = (
    formula(
        "planning",
        "pomodoro_plan",
        "Pomodoro Plan",
        "Turn work and break intervals into a session timeline.",
        (
            p("work_minutes", 25.0, "Minutes per focus block."),
            p("break_minutes", 5.0, "Minutes per break."),
            p("rounds", 4.0, "Focus rounds."),
        ),
        (
            ("Focus minutes", "work_minutes * rounds"),
            ("Break minutes", "break_minutes * max(0, rounds - 1)"),
            (
                "Session minutes",
                "work_minutes * rounds + break_minutes * max(0, rounds - 1)",
            ),
        ),
        (
            (
                "work_minutes <= 0 or break_minutes < 0 or rounds < 1",
                "work and rounds must be positive",
            ),
        ),
    ),
    formula(
        "planning",
        "hydration_goal",
        "Hydration Goal",
        "Estimate a simple daily water goal from body weight and activity.",
        (
            p("weight_kg", 70.0, "Body weight."),
            p("activity_minutes", 45.0, "Active minutes."),
        ),
        (
            ("Base liters", "weight_kg * 0.033"),
            ("Activity liters", "activity_minutes / 30 * 0.35"),
            ("Total liters", "weight_kg * 0.033 + activity_minutes / 30 * 0.35"),
        ),
        (
            (
                "weight_kg <= 0 or activity_minutes < 0",
                "weight must be positive and activity nonnegative",
            ),
        ),
    ),
    formula(
        "planning",
        "sleep_cycle_planner",
        "Sleep Cycle Planner",
        "Estimate sleep duration and cycle count between bedtime and wake time.",
        (
            p("bed_hour", 23.0, "Bedtime decimal hour."),
            p("wake_hour", 7.0, "Wake decimal hour."),
        ),
        (
            ("Sleep hours", "(wake_hour - bed_hour) % 24"),
            ("Approximate cycles", "((wake_hour - bed_hour) % 24) * 60 / 90"),
        ),
        (
            (
                "bed_hour < 0 or bed_hour >= 24 or wake_hour < 0 or wake_hour >= 24",
                "hours must be between 0 and 24",
            ),
        ),
    ),
    formula(
        "planning",
        "budget_allocator",
        "50-30-20 Budget Allocator",
        "Split take-home income into needs, wants, and savings targets.",
        (p("income", 4000.0, "Monthly take-home income."),),
        (
            ("Needs", "income * 0.5"),
            ("Wants", "income * 0.3"),
            ("Savings", "income * 0.2"),
        ),
        (("income < 0", "income cannot be negative"),),
    ),
    formula(
        "planning",
        "debt_payoff",
        "Debt Payoff Estimator",
        "Estimate payoff time without interest using a fixed monthly payment.",
        (
            p("balance", 7500.0, "Debt balance."),
            p("monthly_payment", 375.0, "Monthly payment."),
        ),
        (
            ("Months", "balance / monthly_payment"),
            ("Years", "balance / monthly_payment / 12"),
        ),
        (
            (
                "balance < 0 or monthly_payment <= 0",
                "balance cannot be negative and payment must be positive",
            ),
        ),
    ),
    formula(
        "planning",
        "study_scheduler",
        "Study Scheduler",
        "Allocate study time evenly across subjects and days.",
        (
            p("total_hours", 12.0, "Total study hours."),
            p("subjects", 3.0, "Subject count."),
            p("days", 6.0, "Study days."),
        ),
        (
            ("Hours per subject", "total_hours / subjects"),
            ("Hours per day", "total_hours / days"),
            ("Minutes per subject per day", "total_hours * 60 / subjects / days"),
        ),
        (
            (
                "total_hours < 0 or subjects <= 0 or days <= 0",
                "subjects and days must be positive",
            ),
        ),
    ),
    formula(
        "planning",
        "reading_plan",
        "Reading Plan",
        "Estimate daily pages and reading time for a deadline.",
        (
            p("pages", 360.0, "Pages remaining."),
            p("days", 24.0, "Days available."),
            p("minutes_per_page", 1.5, "Average reading pace."),
        ),
        (
            ("Pages per day", "pages / days"),
            ("Minutes per day", "pages / days * minutes_per_page"),
        ),
        (("pages < 0 or days <= 0 or minutes_per_page < 0", "days must be positive"),),
    ),
    formula(
        "planning",
        "travel_budget",
        "Travel Budget",
        "Estimate total trip cost from daily and fixed expenses.",
        (
            p("days", 7.0, "Trip days."),
            p("lodging_per_day", 120.0, "Daily lodging."),
            p("food_per_day", 55.0, "Daily food."),
            p("transport", 350.0, "Fixed transport."),
            p("buffer_percent", 10.0, "Contingency percent."),
        ),
        (
            ("Base cost", "days * (lodging_per_day + food_per_day) + transport"),
            (
                "Buffer",
                "(days * (lodging_per_day + food_per_day) + transport) * buffer_percent / 100",
            ),
            (
                "Total budget",
                "(days * (lodging_per_day + food_per_day) + transport) * (1 + buffer_percent / 100)",
            ),
        ),
        (
            (
                "days <= 0 or min(lodging_per_day, food_per_day, transport, buffer_percent) < 0",
                "costs cannot be negative",
            ),
        ),
    ),
    formula(
        "planning",
        "meal_portion",
        "Meal Portion Planner",
        "Scale meal portions across people and meals.",
        (
            p("grams_per_person", 180.0, "Ingredient grams per person."),
            p("people", 5.0, "People served."),
            p("meals", 2.0, "Number of meals."),
        ),
        (
            ("Total grams", "grams_per_person * people * meals"),
            ("Total kilograms", "grams_per_person * people * meals / 1000"),
        ),
        (
            (
                "grams_per_person < 0 or people <= 0 or meals <= 0",
                "people and meals must be positive",
            ),
        ),
    ),
    formula(
        "planning",
        "workout_volume",
        "Workout Volume Planner",
        "Calculate resistance-training volume from sets, reps, and weight.",
        (
            p("sets", 4.0, "Set count."),
            p("reps", 8.0, "Repetitions per set."),
            p("weight_kg", 60.0, "Weight per repetition."),
            p("exercises", 3.0, "Exercise count."),
        ),
        (
            ("Total repetitions", "sets * reps * exercises"),
            ("Training volume kg", "sets * reps * weight_kg * exercises"),
        ),
        (
            (
                "sets <= 0 or reps <= 0 or weight_kg < 0 or exercises <= 0",
                "counts must be positive",
            ),
        ),
    ),
    formula(
        "planning",
        "weekly_goal_splitter",
        "Weekly Goal Splitter",
        "Break a measurable goal into weekday and weekend targets.",
        (
            p("goal", 100.0, "Weekly target units."),
            p("weekday_percent", 70.0, "Percent assigned to weekdays."),
        ),
        (
            ("Weekday total", "goal * weekday_percent / 100"),
            ("Per weekday", "goal * weekday_percent / 100 / 5"),
            ("Per weekend day", "goal * (1 - weekday_percent / 100) / 2"),
        ),
        (
            (
                "goal < 0 or weekday_percent < 0 or weekday_percent > 100",
                "percent must be between 0 and 100",
            ),
        ),
    ),
    formula(
        "planning",
        "emergency_fund",
        "Emergency Fund Planner",
        "Estimate emergency-fund target and funding time.",
        (
            p("monthly_expenses", 2800.0, "Essential monthly expenses."),
            p("months", 6.0, "Months of coverage."),
            p("current", 4000.0, "Current fund."),
            p("monthly_saving", 500.0, "Monthly contribution."),
        ),
        (
            ("Target", "monthly_expenses * months"),
            ("Gap", "max(0, monthly_expenses * months - current)"),
            (
                "Months to target",
                "max(0, monthly_expenses * months - current) / monthly_saving",
            ),
        ),
        (
            (
                "monthly_expenses < 0 or months <= 0 or current < 0 or monthly_saving <= 0",
                "coverage and saving must be positive",
            ),
        ),
    ),
    formula(
        "planning",
        "retirement_contribution",
        "Retirement Contribution Planner",
        "Estimate annual retirement contributions including employer match.",
        (
            p("salary", 70000.0, "Annual salary."),
            p("employee_percent", 8.0, "Employee contribution percent."),
            p("match_percent", 4.0, "Employer match percent."),
        ),
        (
            ("Employee annual", "salary * employee_percent / 100"),
            ("Employer annual", "salary * match_percent / 100"),
            ("Combined annual", "salary * (employee_percent + match_percent) / 100"),
        ),
        (
            (
                "salary < 0 or employee_percent < 0 or match_percent < 0",
                "inputs cannot be negative",
            ),
        ),
    ),
    formula(
        "planning",
        "freelance_rate",
        "Freelance Rate Planner",
        "Estimate an hourly freelance rate from income and overhead goals.",
        (
            p("annual_income", 80000.0, "Desired personal income."),
            p("billable_hours", 1200.0, "Annual billable hours."),
            p("overhead_percent", 25.0, "Business overhead percent."),
        ),
        (
            ("Base hourly", "annual_income / billable_hours"),
            (
                "Target hourly",
                "annual_income / billable_hours * (1 + overhead_percent / 100)",
            ),
        ),
        (
            (
                "annual_income < 0 or billable_hours <= 0 or overhead_percent < 0",
                "hours must be positive",
            ),
        ),
    ),
    formula(
        "planning",
        "meeting_cost",
        "Meeting Cost Estimator",
        "Estimate labor cost of a meeting.",
        (
            p("people", 6.0, "Attendee count."),
            p("minutes", 45.0, "Meeting length."),
            p("average_hourly_rate", 55.0, "Average loaded hourly cost."),
        ),
        (
            ("Person-hours", "people * minutes / 60"),
            ("Estimated cost", "people * minutes / 60 * average_hourly_rate"),
        ),
        (
            (
                "people <= 0 or minutes < 0 or average_hourly_rate < 0",
                "people must be positive",
            ),
        ),
    ),
    formula(
        "planning",
        "commute_time",
        "Commute Time Planner",
        "Estimate weekly and annual commute time.",
        (
            p("minutes_one_way", 35.0, "One-way commute minutes."),
            p("days_per_week", 5.0, "Commute days weekly."),
            p("work_weeks", 48.0, "Working weeks yearly."),
        ),
        (
            ("Weekly hours", "minutes_one_way * 2 * days_per_week / 60"),
            ("Annual hours", "minutes_one_way * 2 * days_per_week * work_weeks / 60"),
            (
                "Annual days",
                "minutes_one_way * 2 * days_per_week * work_weeks / 60 / 24",
            ),
        ),
        (
            (
                "minutes_one_way < 0 or days_per_week < 0 or work_weeks < 0",
                "inputs cannot be negative",
            ),
        ),
    ),
    formula(
        "planning",
        "garden_spacing",
        "Garden Spacing Planner",
        "Estimate plant capacity for a rectangular garden bed.",
        (
            p("length_m", 3.0, "Bed length."),
            p("width_m", 1.2, "Bed width."),
            p("spacing_cm", 30.0, "Plant spacing."),
        ),
        (
            ("Area square meters", "length_m * width_m"),
            ("Approximate plants", "length_m * width_m / (spacing_cm / 100) ** 2"),
        ),
        (
            (
                "length_m <= 0 or width_m <= 0 or spacing_cm <= 0",
                "dimensions must be positive",
            ),
        ),
    ),
    formula(
        "planning",
        "pet_food_plan",
        "Pet Food Planner",
        "Estimate food needed and cost over a planning period.",
        (
            p("grams_per_day", 320.0, "Daily food grams."),
            p("days", 30.0, "Planning days."),
            p("price_per_kg", 8.5, "Food price per kilogram."),
        ),
        (
            ("Food kilograms", "grams_per_day * days / 1000"),
            ("Estimated cost", "grams_per_day * days / 1000 * price_per_kg"),
        ),
        (
            (
                "grams_per_day < 0 or days <= 0 or price_per_kg < 0",
                "days must be positive",
            ),
        ),
    ),
    formula(
        "planning",
        "battery_runtime",
        "Battery Runtime Estimator",
        "Estimate ideal battery runtime from capacity and device draw.",
        (
            p("capacity_wh", 500.0, "Battery capacity in watt-hours."),
            p("draw_watts", 85.0, "Average device power draw."),
            p("efficiency_percent", 85.0, "Usable efficiency percent."),
        ),
        (
            ("Usable watt-hours", "capacity_wh * efficiency_percent / 100"),
            ("Runtime hours", "capacity_wh * efficiency_percent / 100 / draw_watts"),
        ),
        (
            (
                "capacity_wh <= 0 or draw_watts <= 0 or efficiency_percent <= 0 or efficiency_percent > 100",
                "inputs must be positive and efficiency at most 100",
            ),
        ),
    ),
    formula(
        "planning",
        "commute_emissions",
        "Commute Emissions Estimator",
        "Estimate travel emissions using a configurable per-kilometer factor.",
        (
            p("distance_km", 18.0, "One-way distance."),
            p("days", 220.0, "Commute days."),
            p("kg_co2_per_km", 0.171, "Emissions factor."),
        ),
        (
            ("Annual kilometers", "distance_km * 2 * days"),
            ("Annual kg CO2e", "distance_km * 2 * days * kg_co2_per_km"),
        ),
        (
            (
                "distance_km < 0 or days < 0 or kg_co2_per_km < 0",
                "inputs cannot be negative",
            ),
        ),
    ),
    formula(
        "planning",
        "event_capacity",
        "Event Capacity Planner",
        "Estimate table count and floor-space needs for an event.",
        (
            p("guests", 120.0, "Expected guests."),
            p("seats_per_table", 8.0, "Seats at each table."),
            p("square_meters_per_guest", 1.5, "Floor area per guest."),
        ),
        (
            ("Tables", "guests / seats_per_table"),
            ("Floor area square meters", "guests * square_meters_per_guest"),
        ),
        (
            (
                "guests <= 0 or seats_per_table <= 0 or square_meters_per_guest <= 0",
                "all inputs must be positive",
            ),
        ),
    ),
)


def text_app(
    category: str,
    slug: str,
    title: str,
    summary: str,
    default_text: str,
    body: str,
    imports: tuple[str, ...] = (),
) -> TextApp:
    """Build text app specification."""
    return TextApp(category, slug, title, summary, default_text, body, imports)


TEXT_TOOLS: tuple[AppSpec, ...] = (
    text_app(
        "text_tools",
        "word_counter",
        "Word Counter",
        "Count lines, words, and characters in text.",
        "Python makes small tools pleasant to build.\nThis is line two.",
        """
        words = text.split()
        lines = text.splitlines() or [""]
        return f"Lines: {len(lines)}\\nWords: {len(words)}\\nCharacters: {len(text)}"
        """,
    ),
    text_app(
        "text_tools",
        "reading_time",
        "Reading Time Estimator",
        "Estimate reading and speaking time from word count.",
        "Clear writing helps readers move quickly through an idea.",
        """
        word_count = len(text.split())
        return (
            f"Words: {word_count}\\n"
            f"Reading minutes: {word_count / 200:.2f}\\n"
            f"Speaking minutes: {word_count / 130:.2f}"
        )
        """,
    ),
    text_app(
        "text_tools",
        "slugifier",
        "Slugifier",
        "Turn a title into a lowercase URL-friendly slug.",
        "Ten Tiny Python Tools!",
        """
        lowered = text.casefold().strip()
        return re.sub(r"[^a-z0-9]+", "-", lowered).strip("-")
        """,
        ("import re",),
    ),
    text_app(
        "text_tools",
        "caesar_cipher",
        "Caesar Cipher",
        "Encode text with a classic three-letter Caesar shift.",
        "Meet me by the old oak tree.",
        """
        result: list[str] = []
        for character in text:
            if character.isascii() and character.isalpha():
                base = ord("A" if character.isupper() else "a")
                result.append(chr((ord(character) - base + 3) % 26 + base))
            else:
                result.append(character)
        return "".join(result)
        """,
    ),
    text_app(
        "text_tools",
        "rot13_encoder",
        "ROT13 Encoder",
        "Apply the reversible ROT13 substitution to text.",
        "The treasure is under the bridge.",
        """
        return codecs.encode(text, "rot_13")
        """,
        ("import codecs",),
    ),
    text_app(
        "text_tools",
        "palindrome_checker",
        "Palindrome Checker",
        "Check whether text reads the same after normalization.",
        "Never odd or even",
        """
        normalized = "".join(character.casefold() for character in text if character.isalnum())
        return f"Normalized: {normalized}\\nPalindrome: {normalized == normalized[::-1]}"
        """,
    ),
    text_app(
        "text_tools",
        "anagram_checker",
        "Anagram Checker",
        "Compare two phrases separated by a vertical bar for anagram equality.",
        "Dormitory | Dirty room",
        """
        left, separator, right = text.partition("|")
        if not separator:
            return "Provide two phrases separated by |"
        def normalize(value: str) -> list[str]:
            return sorted(character.casefold() for character in value if character.isalnum())

        return f"Anagram: {normalize(left) == normalize(right)}"
        """,
    ),
    text_app(
        "text_tools",
        "smart_title_case",
        "Smart Title Case",
        "Capitalize a heading while keeping short connector words lowercase.",
        "a walk through the city of glass",
        """
        small_words = {"a", "an", "and", "as", "at", "by", "for", "in", "of", "on", "or", "the", "to"}
        words = text.casefold().split()
        titled = [word.capitalize() if index in {0, len(words) - 1} or word not in small_words else word for index, word in enumerate(words)]
        return " ".join(titled)
        """,
    ),
    text_app(
        "text_tools",
        "duplicate_line_remover",
        "Duplicate Line Remover",
        "Remove repeated lines while preserving first-seen order.",
        "apple\nbanana\napple\npear\nbanana",
        """
        seen: set[str] = set()
        unique: list[str] = []
        for line in text.splitlines():
            if line not in seen:
                seen.add(line)
                unique.append(line)
        return "\\n".join(unique)
        """,
    ),
    text_app(
        "text_tools",
        "word_frequency",
        "Word Frequency Counter",
        "List words by descending frequency.",
        "Red fish blue fish, one fish two fish.",
        """
        words = re.findall(r"[\\w']+", text.casefold())
        counts = Counter(words)
        return "\\n".join(f"{word}: {count}" for word, count in counts.most_common())
        """,
        ("import re", "from collections import Counter"),
    ),
    text_app(
        "text_tools",
        "line_sorter",
        "Line Sorter",
        "Sort nonempty text lines case-insensitively.",
        "Zebra\napple\nMoon\nbanana",
        """
        return "\\n".join(sorted((line for line in text.splitlines() if line.strip()), key=str.casefold))
        """,
    ),
    text_app(
        "text_tools",
        "markdown_link_extractor",
        "Markdown Link Extractor",
        "Extract labels and targets from inline Markdown links.",
        "Read [Python](https://python.org) and [PEP 8](https://peps.python.org/pep-0008/).",
        """
        links = re.findall(r"\\[([^]]+)]\\(([^)]+)\\)", text)
        return "\\n".join(f"{label}: {target}" for label, target in links) or "No links found."
        """,
        ("import re",),
    ),
    text_app(
        "text_tools",
        "email_masker",
        "Email Masker",
        "Mask email usernames while preserving domains.",
        "Contact alex.example@example.com or team@school.edu.",
        """
        def mask(match: re.Match[str]) -> str:
            username, domain = match.group(1), match.group(2)
            visible = username[:1]
            return f"{visible}{'*' * max(3, len(username) - 1)}@{domain}"

        return re.sub(r"\\b([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\\.[A-Za-z]{2,})\\b", mask, text)
        """,
        ("import re",),
    ),
    text_app(
        "text_tools",
        "whitespace_cleaner",
        "Whitespace Cleaner",
        "Collapse repeated horizontal whitespace and trim every line.",
        "  Too   many   spaces.  \n  Another    line. ",
        """
        return "\\n".join(" ".join(line.split()) for line in text.splitlines())
        """,
    ),
    text_app(
        "text_tools",
        "initials_maker",
        "Initials Maker",
        "Create initials from a person's or organization's name.",
        "National Aeronautics and Space Administration",
        """
        ignored = {"and", "of", "the"}
        return "".join(word[0].upper() for word in text.split() if word.casefold() not in ignored)
        """,
    ),
    text_app(
        "text_tools",
        "pig_latin",
        "Pig Latin Translator",
        "Translate simple English words into playful Pig Latin.",
        "python scripts are surprisingly handy",
        """
        def convert(word: str) -> str:
            match = re.match(r"([^aeiouAEIOU]*)(.*)", word)
            if match is None:
                return word
            prefix, rest = match.groups()
            return f"{rest}{prefix}ay" if prefix else f"{word}yay"

        return " ".join(convert(word) for word in text.split())
        """,
        ("import re",),
    ),
    text_app(
        "text_tools",
        "morse_encoder",
        "Morse Code Encoder",
        "Encode letters and digits as International Morse code symbols.",
        "SOS Python 3",
        """
        symbols = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]
        codes = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", symbols, strict=True))
        return " / ".join(" ".join(codes.get(character, "?") for character in word.upper()) for word in text.split())
        """,
    ),
    text_app(
        "text_tools",
        "vowel_histogram",
        "Vowel Histogram",
        "Count each vowel and draw a small text histogram.",
        "Education is an adventure.",
        """
        lowered = text.casefold()
        return "\\n".join(f"{vowel}: {'#' * lowered.count(vowel)} ({lowered.count(vowel)})" for vowel in "aeiou")
        """,
    ),
    text_app(
        "text_tools",
        "sentence_stats",
        "Sentence Statistics",
        "Summarize sentence count and average sentence length.",
        "Short tools teach ideas. They also solve real problems! Try changing this text?",
        """
        sentences = [part.strip() for part in re.split(r"[.!?]+", text) if part.strip()]
        words = text.split()
        average = len(words) / len(sentences) if sentences else 0.0
        return (
            f"Sentences: {len(sentences)}\\n"
            f"Words: {len(words)}\\n"
            f"Average words: {average:.2f}"
        )
        """,
        ("import re",),
    ),
    text_app(
        "text_tools",
        "password_strength",
        "Password Strength Coach",
        "Score password variety and length without storing the input.",
        "Correct-Horse-9-Battery!",
        """
        checks = {
            "12+ characters": len(text) >= 12,
            "lowercase": any(character.islower() for character in text),
            "uppercase": any(character.isupper() for character in text),
            "digit": any(character.isdigit() for character in text),
            "symbol": any(not character.isalnum() for character in text),
        }
        score = sum(checks.values())
        details = "\\n".join(f"[{'x' if passed else ' '}] {label}" for label, passed in checks.items())
        return f"Score: {score}/{len(checks)}\\n{details}"
        """,
    ),
)


DEVELOPER: tuple[AppSpec, ...] = (
    text_app(
        "developer",
        "base64_encoder",
        "Base64 Encoder",
        "Encode UTF-8 text as Base64.",
        "Python bytes are explicit.",
        "return base64.b64encode(text.encode()).decode()",
        ("import base64",),
    ),
    text_app(
        "developer",
        "url_encoder",
        "URL Encoder",
        "Percent-encode text for safe URL query use.",
        "tea & biscuits / 2",
        "return urllib.parse.quote(text, safe='')",
        ("import urllib.parse",),
    ),
    text_app(
        "developer",
        "deterministic_uuid",
        "Deterministic UUID",
        "Create a stable UUID from a text namespace value.",
        "example-project/item-42",
        "return str(uuid.uuid5(uuid.NAMESPACE_URL, text))",
        ("import uuid",),
    ),
    text_app(
        "developer",
        "hash_text",
        "Text Hashes",
        "Calculate SHA-256 and SHA-512 digests for text.",
        "hash this reproducibly",
        """
        encoded = text.encode()
        return (
            f"SHA-256: {hashlib.sha256(encoded).hexdigest()}\\n"
            f"SHA-512: {hashlib.sha512(encoded).hexdigest()}"
        )
        """,
        ("import hashlib",),
    ),
    text_app(
        "developer",
        "jwt_payload_decoder",
        "JWT Payload Decoder",
        "Decode a JWT payload locally without claiming signature verification.",
        "eyJhbGciOiJub25lIn0.eyJzdWIiOiJkZW1vIiwicm9sZSI6InJlYWRlciJ9.",
        """
        parts = text.split(".")
        if len(parts) != 3:
            return "Expected three dot-separated JWT sections."
        payload = parts[1] + "=" * (-len(parts[1]) % 4)
        decoded = base64.urlsafe_b64decode(payload).decode()
        return json.dumps(json.loads(decoded), indent=2, sort_keys=True)
        """,
        ("import base64", "import json"),
    ),
    text_app(
        "developer",
        "regex_tester",
        "Regex Tester",
        "Test a regular expression against text separated by a vertical bar.",
        r"\bP\w+ | Python powers practical projects",
        """
        pattern, separator, sample = text.partition("|")
        if not separator:
            return "Use PATTERN | TEXT"
        matches = re.findall(pattern.strip(), sample.strip())
        return f"Matches: {len(matches)}\\n{matches!r}"
        """,
        ("import re",),
    ),
    text_app(
        "developer",
        "unified_diff",
        "Unified Diff Maker",
        "Compare two short text blocks separated by a vertical bar.",
        "alpha\nbeta | alpha\ngamma",
        """
        before, separator, after = text.partition("|")
        if not separator:
            return "Use BEFORE | AFTER"
        return "".join(difflib.unified_diff(before.strip().splitlines(keepends=True), after.strip().splitlines(keepends=True), fromfile="before", tofile="after")) or "No differences."
        """,
        ("import difflib",),
    ),
    text_app(
        "developer",
        "text_to_hex",
        "Text to Hex",
        "Show UTF-8 bytes as hexadecimal and decimal values.",
        "Python 🐍",
        """
        encoded = text.encode()
        return f"Hex: {encoded.hex(' ')}\\nBytes: {' '.join(str(value) for value in encoded)}"
        """,
    ),
    text_app(
        "developer",
        "unix_timestamp",
        "Unix Timestamp Converter",
        "Convert an ISO-8601 datetime into a Unix timestamp.",
        "2026-01-01T12:00:00+00:00",
        """
        moment = datetime.fromisoformat(text)
        if moment.tzinfo is None:
            moment = moment.replace(tzinfo=UTC)
        return (
            f"Unix seconds: {moment.timestamp():.0f}\\n"
            f"UTC: {moment.astimezone(UTC).isoformat()}"
        )
        """,
        ("from datetime import UTC, datetime",),
    ),
    text_app(
        "developer",
        "cron_explainer",
        "Cron Field Explainer",
        "Explain the five fields of a basic cron expression.",
        "15 9 * * 1-5",
        """
        fields = text.split()
        if len(fields) != 5:
            return "Expected: minute hour day-of-month month day-of-week"
        labels = ("Minute", "Hour", "Day of month", "Month", "Day of week")
        return "\\n".join(f"{label}: {value}" for label, value in zip(labels, fields, strict=True))
        """,
    ),
    text_app(
        "developer",
        "sql_keyword_formatter",
        "SQL Keyword Formatter",
        "Uppercase common SQL keywords and place major clauses on new lines.",
        "select name, score from players where score > 10 order by score desc",
        """
        keywords = ("select", "from", "where", "group by", "order by", "having", "limit", "join", "on", "as", "and", "or", "desc", "asc")
        result = text
        for keyword in keywords:
            replacement = keyword.upper()
            if keyword in {"from", "where", "group by", "order by", "having", "limit", "join"}:
                replacement = f"\\n{replacement}"
            result = re.sub(rf"\\b{keyword}\\b", replacement, result, flags=re.IGNORECASE)
        return result.strip()
        """,
        ("import re",),
    ),
    text_app(
        "developer",
        "env_diff",
        "Environment Diff",
        "Compare KEY=VALUE blocks separated by a vertical bar without changing files.",
        "MODE=dev\nPORT=8000 | MODE=prod\nPORT=8000\nCACHE=on",
        """
        left, separator, right = text.partition("|")
        if not separator:
            return "Use ENV_A | ENV_B"
        def parse(block: str) -> dict[str, str]:
            return dict(line.split("=", 1) for line in block.strip().splitlines() if "=" in line)
        first, second = parse(left), parse(right)
        keys = sorted(first.keys() | second.keys())
        return "\\n".join(f"{key}: {first.get(key, '<missing>')} -> {second.get(key, '<missing>')}" for key in keys if first.get(key) != second.get(key)) or "No differences."
        """,
    ),
    text_app(
        "developer",
        "semantic_version_compare",
        "Semantic Version Compare",
        "Compare two numeric semantic versions separated by a vertical bar.",
        "2.4.1 | 2.5.0",
        """
        left, separator, right = text.partition("|")
        if not separator:
            return "Use VERSION_A | VERSION_B"
        def parse(value: str) -> tuple[int, int, int]:
            pieces = value.strip().lstrip("v").split(".")
            if len(pieces) != 3:
                error_message = "versions need three numeric parts"
                raise ValueError(error_message)
            return int(pieces[0]), int(pieces[1]), int(pieces[2])
        first, second = parse(left), parse(right)
        relation = "equal to" if first == second else ("older than" if first < second else "newer than")
        return f"{left.strip()} is {relation} {right.strip()}"
        """,
    ),
    text_app(
        "developer",
        "chmod_calculator",
        "Chmod Calculator",
        "Convert a three-digit Unix permission mode into symbolic form.",
        "754",
        """
        if len(text) != 3 or any(character not in "01234567" for character in text):
            return "Provide a three-digit octal mode, such as 754."
        symbols = ""
        for digit in text:
            value = int(digit)
            symbols += "r" if value & 4 else "-"
            symbols += "w" if value & 2 else "-"
            symbols += "x" if value & 1 else "-"
        return f"{text}: {symbols}"
        """,
    ),
    text_app(
        "developer",
        "http_status_lookup",
        "HTTP Status Lookup",
        "Look up the standard phrase for an HTTP status code.",
        "418",
        """
        try:
            status = HTTPStatus(int(text))
        except (ValueError, TypeError):
            return "Unknown or invalid HTTP status."
        return f"{status.value} {status.phrase}\\n{status.description}"
        """,
        ("from http import HTTPStatus",),
    ),
    text_app(
        "developer",
        "color_converter",
        "Color Converter",
        "Convert a six-digit hexadecimal color to RGB and HSL.",
        "#4f86c6",
        """
        value = text.strip().lstrip("#")
        if not re.fullmatch(r"[0-9a-fA-F]{6}", value):
            return "Provide a six-digit hex color."
        red, green, blue = (int(value[index:index + 2], 16) for index in (0, 2, 4))
        hue, lightness, saturation = colorsys.rgb_to_hls(red / 255, green / 255, blue / 255)
        return (
            f"RGB: {red}, {green}, {blue}\\n"
            f"HSL: {hue * 360:.0f}°, {saturation * 100:.0f}%, "
            f"{lightness * 100:.0f}%"
        )
        """,
        ("import colorsys", "import re"),
    ),
    text_app(
        "developer",
        "lorem_generator",
        "Lorem Generator",
        "Generate a deterministic filler paragraph from a numeric word count.",
        "40",
        """
        words = ["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua"]
        try:
            count = max(1, min(500, int(text)))
        except ValueError:
            return "Provide a word count from 1 to 500."
        return " ".join(words[index % len(words)] for index in range(count)).capitalize() + "."
        """,
    ),
    text_app(
        "developer",
        "fake_record_generator",
        "Fake Record Generator",
        "Create deterministic fictional test data from a seed phrase.",
        "demo-seed",
        """
        digest = hashlib.sha256(text.encode()).digest()
        first_names = ("Avery", "Jordan", "Morgan", "Riley", "Taylor")
        last_names = ("Quinn", "Rivera", "Patel", "Kim", "Okafor")
        first = first_names[digest[0] % len(first_names)]
        last = last_names[digest[1] % len(last_names)]
        number = int.from_bytes(digest[2:4]) % 10000
        return json.dumps({"name": f"{first} {last}", "email": f"{first.casefold()}.{last.casefold()}{number}@example.test", "id": number}, indent=2)
        """,
        ("import hashlib", "import json"),
    ),
    text_app(
        "developer",
        "markdown_table_maker",
        "Markdown Table Maker",
        "Convert semicolon-separated rows and comma-separated cells into a Markdown table.",
        "Name,Score;Ada,98;Grace,96",
        """
        rows = [[cell.strip() for cell in row.split(",")] for row in text.split(";")]
        if len(rows) < 2 or not rows[0]:
            return "Provide a header and at least one row."
        width = len(rows[0])
        if any(len(row) != width for row in rows):
            return "Every row must have the same cell count."
        header = "| " + " | ".join(rows[0]) + " |"
        divider = "| " + " | ".join("---" for _ in rows[0]) + " |"
        body_rows = ["| " + " | ".join(row) + " |" for row in rows[1:]]
        return "\\n".join((header, divider, *body_rows))
        """,
    ),
    text_app(
        "developer",
        "query_string_parser",
        "Query String Parser",
        "Parse a URL query string into readable key-value pairs.",
        "page=2&tag=python&tag=tools&sort=new",
        """
        values = urllib.parse.parse_qs(text, keep_blank_values=True)
        return "\\n".join(f"{key}: {', '.join(items)}" for key, items in sorted(values.items())) or "No parameters."
        """,
        ("import urllib.parse",),
    ),
    text_app(
        "developer",
        "subnet_inspector",
        "Subnet Inspector",
        "Inspect an IPv4 or IPv6 network in CIDR notation.",
        "192.168.10.42/24",
        """
        interface = ipaddress.ip_interface(text.strip())
        network = interface.network
        return (
            f"Address: {interface.ip}\\n"
            f"Network: {network}\\n"
            f"Addresses: {network.num_addresses}\\n"
            f"Private: {interface.ip.is_private}"
        )
        """,
        ("import ipaddress",),
    ),
)


def generator(
    slug: str,
    title: str,
    summary: str,
    pattern: str,
    banks: tuple[tuple[str, tuple[str, ...]], ...],
) -> GeneratorApp:
    """Build creative generator specification."""
    return GeneratorApp("creative", slug, title, summary, pattern, banks)


CREATIVE: tuple[AppSpec, ...] = (
    generator(
        "story_prompt",
        "Story Prompt Generator",
        "Combine a protagonist, goal, obstacle, and setting into writing prompts.",
        "A {protagonist} must {goal}, but {obstacle}, in {setting}.",
        (
            (
                "protagonist",
                (
                    "retired cartographer",
                    "curious robot",
                    "forgetful magician",
                    "night-shift baker",
                ),
            ),
            (
                "goal",
                (
                    "decode a moving map",
                    "return a borrowed moon",
                    "save a silent festival",
                    "find the owner of a memory",
                ),
            ),
            (
                "obstacle",
                (
                    "time runs backward",
                    "every clue contradicts the last",
                    "the town refuses to wake",
                    "their shadow has other plans",
                ),
            ),
            (
                "setting",
                (
                    "a city built on bridges",
                    "an underwater library",
                    "the last train in winter",
                    "a village inside a clock",
                ),
            ),
        ),
    ),
    generator(
        "character_builder",
        "Character Builder",
        "Create compact character concepts with motivations and contradictions.",
        "{name}, a {role}, wants {goal} but secretly {secret}; signature habit: {habit}.",
        (
            ("name", ("Arin Vale", "Mira Moss", "Jun Ember", "Sol Marrow")),
            (
                "role",
                (
                    "weather archivist",
                    "monster mediator",
                    "orbital gardener",
                    "dream locksmith",
                ),
            ),
            (
                "goal",
                (
                    "a quiet life",
                    "public recognition",
                    "to repair one mistake",
                    "a place to belong",
                ),
            ),
            (
                "secret",
                (
                    "fears silence",
                    "caused the central problem",
                    "can hear machines think",
                    "is living under a borrowed name",
                ),
            ),
            (
                "habit",
                (
                    "collects blue buttons",
                    "answers questions with recipes",
                    "hums before lying",
                    "writes notes to tomorrow",
                ),
            ),
        ),
    ),
    generator(
        "fantasy_name",
        "Fantasy Name Generator",
        "Generate pronounceable fantasy place and character names.",
        "{prefix}{middle}{suffix}",
        (
            ("prefix", ("Ael", "Vor", "Mira", "Thorn", "Kael")),
            ("middle", ("an", "ori", "eth", "ul", "ava")),
            ("suffix", ("dor", "wyn", "is", "ara", "en")),
        ),
    ),
    generator(
        "haiku_seed",
        "Haiku Seed Generator",
        "Offer three vivid image fragments for drafting a haiku.",
        "{season} / {motion} / {turn}",
        (
            (
                "season",
                (
                    "first autumn frost",
                    "warm summer thunder",
                    "late spring rain",
                    "winter moonlight",
                ),
            ),
            (
                "motion",
                (
                    "a moth circles home",
                    "river stones listen",
                    "one red leaf lets go",
                    "cloud shadows wander",
                ),
            ),
            (
                "turn",
                (
                    "the empty cup sings",
                    "your old name returns",
                    "nothing needs an answer",
                    "morning opens slowly",
                ),
            ),
        ),
    ),
    generator(
        "color_palette",
        "Color Palette Namer",
        "Invent themed color-palette briefs for visual projects.",
        "{mood} palette: {color1}, {color2}, {color3}; use for {use}.",
        (
            (
                "mood",
                ("quiet cosmic", "sunlit workshop", "rainy arcade", "desert library"),
            ),
            ("color1", ("indigo ink", "copper glow", "moss green", "cloud white")),
            ("color2", ("electric coral", "paper cream", "storm blue", "plum shadow")),
            ("color3", ("mint signal", "charcoal", "amber glass", "rose dust")),
            (
                "use",
                ("an album cover", "a reading app", "a board game", "a poster series"),
            ),
        ),
    ),
    generator(
        "chord_progression",
        "Chord Progression Generator",
        "Suggest song sections using Roman-numeral chord progressions.",
        "{section}: {progression} in a {feel} feel at {tempo} tempo.",
        (
            ("section", ("Verse", "Chorus", "Bridge", "Outro")),
            ("progression", ("I–V–vi–IV", "ii–V–I–vi", "i–VII–VI–VII", "I–iii–IV–iv")),
            (
                "feel",
                ("bright acoustic", "restless synth", "slow cinematic", "playful funk"),
            ),
            ("tempo", ("72 BPM", "96 BPM", "118 BPM", "140 BPM")),
        ),
    ),
    generator(
        "melody_pattern",
        "Melody Pattern Generator",
        "Create scale-degree motifs for melody practice.",
        "Degrees {degrees}; rhythm {rhythm}; shape {shape}.",
        (
            ("degrees", ("1-3-5-2", "5-4-2-1", "1-2-4-6", "3-2-1-7")),
            (
                "rhythm",
                (
                    "long-short-short-long",
                    "four even eighths",
                    "syncopated eighths",
                    "dotted-quarter and three eighths",
                ),
            ),
            (
                "shape",
                (
                    "rise then resolve",
                    "fall by steps",
                    "leap and echo",
                    "circle one anchor note",
                ),
            ),
        ),
    ),
    generator(
        "ascii_pattern",
        "ASCII Pattern Designer",
        "Generate small instructions for text-based geometric art.",
        "Draw {shape} using {symbol}, size {size}, with {twist}.",
        (
            ("shape", ("a diamond", "nested squares", "a wave", "a spiral")),
            ("symbol", ("#", "*", "+", "<>")),
            ("size", ("7", "9", "12", "15")),
            (
                "twist",
                (
                    "alternating gaps",
                    "a mirrored center",
                    "a gradient of density",
                    "one broken edge",
                ),
            ),
        ),
    ),
    generator(
        "dungeon_room",
        "Dungeon Room Generator",
        "Build tabletop dungeon rooms with hazards, clues, and rewards.",
        "{room}; hazard: {hazard}; clue: {clue}; reward: {reward}.",
        (
            (
                "room",
                (
                    "A flooded observatory",
                    "A kitchen frozen mid-feast",
                    "A hall of whispering portraits",
                    "A root-filled chapel",
                ),
            ),
            (
                "hazard",
                (
                    "rising water",
                    "polite mimic furniture",
                    "a repeating minute",
                    "sleeping glass insects",
                ),
            ),
            (
                "clue",
                (
                    "star positions scratched into tile",
                    "a recipe missing one ingredient",
                    "one portrait looks away",
                    "roots spell a name",
                ),
            ),
            (
                "reward",
                (
                    "a compass that points to promises",
                    "a restorative silver apple",
                    "a key made of warm wax",
                    "a map visible only in rain",
                ),
            ),
        ),
    ),
    generator(
        "planet_generator",
        "Planet Generator",
        "Invent science-fiction worlds with environments and mysteries.",
        "{name}: {environment}; inhabited by {inhabitants}; mystery: {mystery}.",
        (
            ("name", ("Oris-7", "Pelagos", "Vanta Minor", "Ilyra")),
            (
                "environment",
                (
                    "floating salt continents",
                    "forests beneath clear ice",
                    "permanent copper twilight",
                    "mountains that migrate",
                ),
            ),
            (
                "inhabitants",
                (
                    "tidal engineers",
                    "archival drones",
                    "nomadic cloud farmers",
                    "echo-based life",
                ),
            ),
            (
                "mystery",
                (
                    "a signal older than its star",
                    "one missing season",
                    "ruins that appear in dreams",
                    "gravity pauses every century",
                ),
            ),
        ),
    ),
    generator(
        "superhero_generator",
        "Superhero Generator",
        "Create unusual heroes with powers, limits, and civic problems.",
        "{alias} can {power}, but {limit}; today they must {problem}.",
        (
            ("alias", ("The Margin", "Static Bloom", "Second Hand", "Mothlight")),
            (
                "power",
                (
                    "step into written footnotes",
                    "grow tools from seeds",
                    "borrow ten seconds from tomorrow",
                    "speak with streetlights",
                ),
            ),
            (
                "limit",
                (
                    "only near a library",
                    "every tool wilts by sunset",
                    "tomorrow becomes shorter",
                    "the lights exaggerate",
                ),
            ),
            (
                "problem",
                (
                    "mediate a parade route",
                    "find a missing bus",
                    "repair a community garden",
                    "stop a rumor becoming real",
                ),
            ),
        ),
    ),
    generator(
        "recipe_idea",
        "Recipe Idea Generator",
        "Combine ingredients, techniques, and flavor directions for cooking experiments.",
        "Try {ingredient} with {partner}, {technique}, finished with {finish}.",
        (
            ("ingredient", ("chickpeas", "sweet potato", "mushrooms", "pears")),
            ("partner", ("smoked paprika", "miso", "rosemary", "toasted sesame")),
            (
                "technique",
                (
                    "roasted until crisp",
                    "folded into flatbread",
                    "simmered into a thick stew",
                    "grilled on skewers",
                ),
            ),
            ("finish", ("lemon yogurt", "chili oil", "fresh herbs", "crushed nuts")),
        ),
    ),
    generator(
        "writing_constraint",
        "Writing Constraint Generator",
        "Create playful constraints for a short writing exercise.",
        "Write {length} about {subject}; {constraint}; include {object}.",
        (
            (
                "length",
                (
                    "exactly 100 words",
                    "one page",
                    "six sentences",
                    "a dialogue-only scene",
                ),
            ),
            (
                "subject",
                (
                    "an unexpected delivery",
                    "the final day of summer",
                    "a tiny rebellion",
                    "a misunderstood machine",
                ),
            ),
            (
                "constraint",
                (
                    "avoid the letter E",
                    "change narrator halfway",
                    "use only present tense",
                    "each sentence gets shorter",
                ),
            ),
            (
                "object",
                (
                    "a green umbrella",
                    "three mismatched socks",
                    "a receipt from the future",
                    "a jar of buttons",
                ),
            ),
        ),
    ),
    generator(
        "metaphor_mixer",
        "Metaphor Mixer",
        "Mix sensory images into surprising metaphor starters.",
        "{concept} is {image} {action}.",
        (
            ("concept", ("Patience", "Jealousy", "Memory", "Hope")),
            (
                "image",
                (
                    "a paper lantern",
                    "an untuned radio",
                    "a winter orchard",
                    "a pocket compass",
                ),
            ),
            (
                "action",
                (
                    "waiting beneath the floorboards",
                    "searching for one clear station",
                    "holding fruit no one can see",
                    "pointing through a storm",
                ),
            ),
        ),
    ),
    generator(
        "plot_twist",
        "Plot Twist Generator",
        "Add fair but surprising reversals to story outlines.",
        "Twist: {reveal}. Earlier clue: {clue}. Cost: {cost}.",
        (
            (
                "reveal",
                (
                    "the rival has protected the hero",
                    "the destination is moving",
                    "the prophecy describes the past",
                    "the missing object chose to leave",
                ),
            ),
            (
                "clue",
                (
                    "every threat arrived too late",
                    "maps disagree by one mile",
                    "all verbs were past tense",
                    "empty footprints face outward",
                ),
            ),
            (
                "cost",
                (
                    "trust becomes harder",
                    "home cannot be found twice",
                    "victory changes nothing",
                    "the truth hurts an ally",
                ),
            ),
        ),
    ),
    generator(
        "npc_dialogue",
        "NPC Dialogue Seed",
        "Generate tabletop NPC voices, needs, and opening lines.",
        "{speaker} ({voice}) needs {need}. Opening: “{line}”",
        (
            (
                "speaker",
                (
                    "harbor clerk",
                    "wandering herbalist",
                    "apprentice ghost",
                    "retired dragon",
                ),
            ),
            (
                "voice",
                (
                    "speaks in lists",
                    "never uses names",
                    "answers too quickly",
                    "pauses for imaginary applause",
                ),
            ),
            (
                "need",
                (
                    "a harmless secret delivered",
                    "help reading a modern map",
                    "someone to verify a strange noise",
                    "a replacement for a lost teacup",
                ),
            ),
            (
                "line",
                (
                    "You look like item three on my agenda.",
                    "The road remembers you.",
                    "No, that sound is definitely new.",
                    "Please ignore the smoke; it is sentimental.",
                ),
            ),
        ),
    ),
    generator(
        "poem_seed",
        "Poem Seed Generator",
        "Offer a title, image, sound, and final-word constraint for a poem.",
        "Title “{title}”; image: {image}; sound: {sound}; end on “{ending}”.",
        (
            (
                "title",
                (
                    "Instructions for Fog",
                    "Small Astronomy",
                    "After the Market",
                    "Borrowed Weather",
                ),
            ),
            (
                "image",
                (
                    "keys cooling on a windowsill",
                    "chalk stars on wet pavement",
                    "oranges rolling from a bag",
                    "a coat holding rain",
                ),
            ),
            (
                "sound",
                (
                    "distant train brakes",
                    "spoons in a drawer",
                    "bees behind a wall",
                    "one bicycle bell",
                ),
            ),
            ("ending", ("home", "blue", "again", "open")),
        ),
    ),
    generator(
        "logo_brief",
        "Logo Brief Generator",
        "Draft compact fictional logo briefs for design practice.",
        "Brand {brand}: {offer}; {personality}; motif {motif}; avoid {avoid}.",
        (
            ("brand", ("Northloop", "Kindling Lab", "Pebble & Pine", "Second Sunrise")),
            (
                "offer",
                (
                    "repair workshops",
                    "science kits",
                    "outdoor stationery",
                    "community breakfast",
                ),
            ),
            (
                "personality",
                (
                    "clever and calm",
                    "warm and experimental",
                    "rugged but precise",
                    "optimistic and local",
                ),
            ),
            (
                "motif",
                (
                    "interlocking path",
                    "controlled spark",
                    "stacked landscape",
                    "rising bowl",
                ),
            ),
            (
                "avoid",
                (
                    "literal tools",
                    "generic atoms",
                    "mountain clichés",
                    "sunburst clichés",
                ),
            ),
        ),
    ),
    generator(
        "worldbuilding_question",
        "Worldbuilding Question Generator",
        "Ask focused questions that expose consequences in fictional worlds.",
        "If {premise}, how does it change {system}, especially for {group}?",
        (
            (
                "premise",
                (
                    "memories can be traded",
                    "night lasts a month",
                    "roads choose destinations",
                    "music controls weather",
                ),
            ),
            (
                "system",
                (
                    "inheritance law",
                    "food storage",
                    "postal service",
                    "public education",
                ),
            ),
            (
                "group",
                (
                    "children",
                    "traveling workers",
                    "rural communities",
                    "people without money",
                ),
            ),
        ),
    ),
    generator(
        "comic_panel",
        "Comic Panel Generator",
        "Create three-beat visual comedy setups for drawing practice.",
        "Panel 1: {setup}. Panel 2: {escalation}. Panel 3: {payoff}.",
        (
            (
                "setup",
                (
                    "A cat studies a blueprint",
                    "A wizard opens tech support",
                    "A robot plants one flower",
                    "A knight waits at a laundromat",
                ),
            ),
            (
                "escalation",
                (
                    "the blueprint studies back",
                    "every caller is a cursed printer",
                    "the flower requests an update",
                    "the washing machines demand a quest",
                ),
            ),
            (
                "payoff",
                (
                    "the cat stamps it approved",
                    "the wizard prescribes turning it off and on",
                    "the robot offers sunshine as a service",
                    "the knight returns with the legendary lost sock",
                ),
            ),
        ),
    ),
)


def quiz(
    slug: str,
    title: str,
    summary: str,
    cards: tuple[tuple[str, str, str], ...],
) -> QuizApp:
    """Build learning quiz specification."""
    return QuizApp("learning", slug, title, summary, cards)


LEARNING: tuple[AppSpec, ...] = (
    quiz(
        "multiplication_trainer",
        "Multiplication Trainer",
        "Practice mental multiplication facts.",
        (
            ("What is 7 × 8?", "56", "Break it into 7 × 4, then double."),
            ("What is 12 × 9?", "108", "Twelve tens minus twelve."),
            ("What is 6 × 7?", "42", "A famous product worth memorizing."),
            (
                "What is 14 × 5?",
                "70",
                "Multiplying by five is half of multiplying by ten.",
            ),
        ),
    ),
    quiz(
        "python_basics",
        "Python Basics Quiz",
        "Review core Python syntax and data types.",
        (
            (
                "Which keyword defines a function?",
                "def",
                "A function starts with def, its name, and parentheses.",
            ),
            (
                "Which built-in type stores key-value pairs?",
                "dict",
                "Dictionary keys map to values.",
            ),
            (
                "What value represents absence?",
                "None",
                "None is Python's null singleton.",
            ),
            (
                "Which keyword starts exception handling?",
                "try",
                "A try block is paired with except or finally.",
            ),
        ),
    ),
    quiz(
        "capital_cities",
        "Capital City Quiz",
        "Practice country and capital pairs.",
        (
            ("Capital of Japan?", "Tokyo", "Tokyo is on Honshu."),
            (
                "Capital of Kenya?",
                "Nairobi",
                "Nairobi lies in Kenya's south-central highlands.",
            ),
            ("Capital of Canada?", "Ottawa", "Ottawa is in Ontario."),
            (
                "Capital of New Zealand?",
                "Wellington",
                "Wellington sits at the southern end of North Island.",
            ),
        ),
    ),
    quiz(
        "periodic_table",
        "Periodic Table Quiz",
        "Review common chemical element symbols.",
        (
            ("Symbol for sodium?", "Na", "Na comes from Latin natrium."),
            ("Symbol for iron?", "Fe", "Fe comes from Latin ferrum."),
            ("Element with symbol K?", "Potassium", "K comes from Latin kalium."),
            (
                "Element with atomic number 6?",
                "Carbon",
                "Carbon anchors organic chemistry.",
            ),
        ),
    ),
    quiz(
        "vocabulary_builder",
        "Vocabulary Builder",
        "Learn precise English vocabulary through short definitions.",
        (
            (
                "Word meaning brief and clear?",
                "concise",
                "Concise expression uses no unnecessary words.",
            ),
            (
                "Word meaning able to recover quickly?",
                "resilient",
                "Resilience is recovery after difficulty.",
            ),
            (
                "Word meaning occurring at irregular intervals?",
                "sporadic",
                "Sporadic events are scattered or occasional.",
            ),
            (
                "Word meaning careful and exact?",
                "meticulous",
                "Meticulous work pays close attention to detail.",
            ),
        ),
    ),
    quiz(
        "binary_numbers",
        "Binary Number Quiz",
        "Practice converting small binary and decimal values.",
        (
            ("Binary 1010 in decimal?", "10", "8 + 2 equals 10."),
            ("Decimal 7 in binary?", "111", "Four plus two plus one."),
            ("Binary 10000 in decimal?", "16", "One in the 2⁴ place."),
            ("Decimal 12 in binary?", "1100", "Eight plus four."),
        ),
    ),
    quiz(
        "prime_numbers",
        "Prime Number Quiz",
        "Review factors and small prime numbers.",
        (
            ("Is 29 prime?", "yes", "No integer from 2 through √29 divides it."),
            ("Smallest prime number?", "2", "Two is the only even prime."),
            ("Prime factors of 21?", "3 and 7", "3 × 7 equals 21."),
            ("Is 1 prime?", "no", "A prime has exactly two positive divisors."),
        ),
    ),
    quiz(
        "fraction_skills",
        "Fraction Skills Quiz",
        "Practice simplifying and comparing fractions.",
        (
            ("Simplify 12/18.", "2/3", "Divide numerator and denominator by 6."),
            ("Which is larger: 3/4 or 2/3?", "3/4", "Cross-products are 9 and 8."),
            ("1/2 + 1/4?", "3/4", "Rewrite one-half as two-fourths."),
            ("Reciprocal of 5/8?", "8/5", "Swap numerator and denominator."),
        ),
    ),
    quiz(
        "statistics_basics",
        "Statistics Basics Quiz",
        "Review mean, median, mode, and range.",
        (
            ("Mean of 2, 4, 6?", "4", "Add values and divide by three."),
            ("Median of 1, 3, 9, 10?", "6", "Average the two middle values, 3 and 9."),
            ("Mode of 2, 2, 3, 4?", "2", "Mode is the most frequent value."),
            ("Range of 5, 8, 12?", "7", "Maximum minus minimum."),
        ),
    ),
    quiz(
        "probability_basics",
        "Probability Basics Quiz",
        "Practice simple event probabilities.",
        (
            ("Chance of heads on a fair coin?", "1/2", "Two equally likely outcomes."),
            (
                "Chance of rolling a 6 on a fair die?",
                "1/6",
                "One favorable face out of six.",
            ),
            (
                "Chance of drawing an ace from 52 cards?",
                "1/13",
                "Four aces divided by 52 cards.",
            ),
            (
                "Probability of an impossible event?",
                "0",
                "Impossible events have probability zero.",
            ),
        ),
    ),
    quiz(
        "physics_motion",
        "Physics Motion Quiz",
        "Review basic speed, acceleration, and force ideas.",
        (
            (
                "Speed equals distance divided by what?",
                "time",
                "Speed measures distance per unit time.",
            ),
            (
                "SI unit of force?",
                "newton",
                "One newton accelerates one kilogram at one meter per second squared.",
            ),
            (
                "Acceleration due to Earth gravity near surface, about?",
                "9.8 m/s²",
                "The value varies slightly by location.",
            ),
            (
                "Momentum equals mass times what?",
                "velocity",
                "Momentum is a vector quantity.",
            ),
        ),
    ),
    quiz(
        "electricity_basics",
        "Electricity Basics Quiz",
        "Review voltage, current, resistance, and power.",
        (
            (
                "Ohm's law for voltage?",
                "V = I × R",
                "Voltage equals current times resistance.",
            ),
            ("Unit of current?", "ampere", "Current is measured in amperes or amps."),
            ("Unit of resistance?", "ohm", "The symbol is Ω."),
            (
                "Electrical power formula?",
                "P = V × I",
                "Power equals voltage times current.",
            ),
        ),
    ),
    quiz(
        "astronomy_basics",
        "Astronomy Basics Quiz",
        "Review solar-system and stellar concepts.",
        (
            (
                "Planet closest to the Sun?",
                "Mercury",
                "Mercury orbits in about 88 Earth days.",
            ),
            ("Our galaxy?", "Milky Way", "The Solar System lies in the Orion Arm."),
            (
                "A star's energy mainly comes from what process?",
                "nuclear fusion",
                "Hydrogen nuclei fuse into helium in main-sequence stars.",
            ),
            (
                "Largest planet in our Solar System?",
                "Jupiter",
                "Jupiter is a gas giant.",
            ),
        ),
    ),
    quiz(
        "geology_basics",
        "Geology Basics Quiz",
        "Learn rock types and Earth structure.",
        (
            (
                "Rock formed from cooled magma?",
                "igneous",
                "Igneous rock crystallizes from molten material.",
            ),
            (
                "Rock changed by heat and pressure?",
                "metamorphic",
                "Metamorphism changes existing rock without fully melting it.",
            ),
            (
                "Earth's outer solid layer?",
                "crust",
                "Oceanic and continental crust differ.",
            ),
            (
                "Scale commonly used for mineral hardness?",
                "Mohs",
                "The Mohs scale ranks scratch resistance.",
            ),
        ),
    ),
    quiz(
        "human_body",
        "Human Body Quiz",
        "Review foundational anatomy and physiology.",
        (
            (
                "Organ that pumps blood?",
                "heart",
                "The heart's chambers drive pulmonary and systemic circulation.",
            ),
            (
                "Largest organ of the body?",
                "skin",
                "Skin protects and regulates temperature.",
            ),
            (
                "Where does most gas exchange occur in lungs?",
                "alveoli",
                "Alveoli provide a large thin surface.",
            ),
            ("Bone protecting the brain?", "skull", "The cranium encloses the brain."),
        ),
    ),
    quiz(
        "music_theory",
        "Music Theory Quiz",
        "Review intervals, scales, and notation.",
        (
            (
                "Notes in a major triad?",
                "root, major third, perfect fifth",
                "Those intervals create its characteristic sound.",
            ),
            (
                "Relative minor of C major?",
                "A minor",
                "They share the same key signature.",
            ),
            (
                "How many semitones in an octave?",
                "12",
                "Western equal temperament divides an octave into twelve.",
            ),
            (
                "Symbol that raises a pitch one semitone?",
                "sharp",
                "A sharp is written ♯.",
            ),
        ),
    ),
    quiz(
        "art_history",
        "Art History Quiz",
        "Connect major art movements with defining ideas.",
        (
            (
                "Movement associated with Monet?",
                "Impressionism",
                "Impressionists explored light and immediate perception.",
            ),
            (
                "Movement using dreamlike unconscious imagery?",
                "Surrealism",
                "Surrealists drew on dreams and unexpected juxtapositions.",
            ),
            (
                "Who painted Guernica?",
                "Pablo Picasso",
                "The mural responds to the bombing of Guernica.",
            ),
            (
                "Renaissance began in which country?",
                "Italy",
                "Italian city-states were early centers.",
            ),
        ),
    ),
    quiz(
        "world_history",
        "World History Quiz",
        "Review selected milestones from world history.",
        (
            (
                "The printing press in Europe is associated with whom?",
                "Johannes Gutenberg",
                "His movable-type system spread in the 15th century.",
            ),
            (
                "The Magna Carta was sealed in what year?",
                "1215",
                "It constrained English royal power.",
            ),
            (
                "Ancient city famous for its library?",
                "Alexandria",
                "The Library of Alexandria was a major Hellenistic center.",
            ),
            (
                "The Silk Roads linked East Asia primarily with what broad region?",
                "Europe",
                "Networks also connected South Asia, Central Asia, and the Middle East.",
            ),
        ),
    ),
    quiz(
        "logical_reasoning",
        "Logical Reasoning Quiz",
        "Practice basic logical operators and implications.",
        (
            ("True AND False?", "false", "AND requires both operands to be true."),
            (
                "True OR False?",
                "true",
                "Inclusive OR requires at least one true operand.",
            ),
            ("NOT True?", "false", "NOT reverses a truth value."),
            (
                "If P implies Q and P is true, what follows?",
                "Q",
                "This valid form is modus ponens.",
            ),
        ),
    ),
    quiz(
        "computer_networks",
        "Computer Networks Quiz",
        "Review practical networking concepts and protocols.",
        (
            (
                "Protocol commonly used for secure web traffic?",
                "HTTPS",
                "HTTPS carries HTTP over TLS.",
            ),
            (
                "DNS maps names to what?",
                "IP addresses",
                "DNS records can hold several kinds of data.",
            ),
            ("Default port for SSH?", "22", "Servers can be configured differently."),
            (
                "Device that forwards packets between networks?",
                "router",
                "Routers make next-hop decisions using routing tables.",
            ),
        ),
    ),
)


def file_app(
    slug: str,
    title: str,
    summary: str,
    body: str,
    imports: tuple[str, ...] = (),
) -> FileApp:
    """Build read-only filesystem app specification."""
    return FileApp("file_tools", slug, title, summary, body, imports)


FILE_TOOLS: tuple[AppSpec, ...] = (
    file_app(
        "directory_tree",
        "Directory Tree",
        "Print a compact, sorted directory tree.",
        """
        if not path.is_dir():
            return path.name
        lines = [f"{path.resolve().name}/"]
        entries = sorted(path.rglob("*"), key=lambda item: item.as_posix().casefold())
        for item in entries[:200]:
            relative = item.relative_to(path)
            prefix = "  " * (len(relative.parts) - 1)
            lines.append(f"{prefix}{relative.name}{'/' if item.is_dir() else ''}")
        if len(entries) > 200:
            lines.append(f"… {len(entries) - 200} more entries")
        return "\\n".join(lines)
        """,
    ),
    file_app(
        "extension_counter",
        "File Extension Counter",
        "Count files by extension beneath a directory.",
        """
        files = [path] if path.is_file() else [item for item in path.rglob("*") if item.is_file()]
        counts = Counter(item.suffix.casefold() or "[no extension]" for item in files)
        return "\\n".join(f"{extension}: {count}" for extension, count in counts.most_common()) or "No files found."
        """,
        ("from collections import Counter",),
    ),
    file_app(
        "disk_usage_report",
        "Disk Usage Report",
        "Summarize file counts and byte usage beneath a path.",
        """
        files = [path] if path.is_file() else [item for item in path.rglob("*") if item.is_file()]
        sizes = [(item, item.stat().st_size) for item in files]
        total = sum(size for _, size in sizes)
        largest = max(sizes, key=lambda pair: pair[1], default=(path, 0))
        return (
            f"Files: {len(files)}\\n"
            f"Total bytes: {total:,}\\n"
            f"Largest: {largest[0]} ({largest[1]:,} bytes)"
        )
        """,
    ),
    file_app(
        "duplicate_file_finder",
        "Duplicate File Finder",
        "Find exact duplicate files using size and SHA-256 without deleting anything.",
        """
        files = [path] if path.is_file() else [item for item in path.rglob("*") if item.is_file()]
        by_size: dict[int, list[Path]] = {}
        for item in files:
            by_size.setdefault(item.stat().st_size, []).append(item)
        by_digest: dict[str, list[Path]] = {}
        for same_size in by_size.values():
            if len(same_size) > 1:
                for item in same_size:
                    digest = hashlib.sha256(item.read_bytes()).hexdigest()
                    by_digest.setdefault(digest, []).append(item)
        groups = [items for items in by_digest.values() if len(items) > 1]
        return "\\n\\n".join("Duplicate group:\\n" + "\\n".join(str(item) for item in items) for items in groups) or "No exact duplicates found."
        """,
        ("import hashlib",),
    ),
    file_app(
        "checksum_maker",
        "Checksum Maker",
        "Calculate SHA-256 checksums for a file or directory.",
        """
        files = [path] if path.is_file() else sorted(item for item in path.rglob("*") if item.is_file())[:100]
        lines = []
        for item in files:
            digest = hashlib.sha256(item.read_bytes()).hexdigest()
            lines.append(f"{digest}  {item}")
        return "\\n".join(lines) or "No files found."
        """,
        ("import hashlib",),
    ),
    file_app(
        "line_statistics",
        "Line Statistics",
        "Count text lines, blank lines, and longest line length.",
        """
        target = path if path.is_file() else next((item for item in path.rglob("*.py") if item.is_file()), None)
        if target is None:
            return "No text candidate found."
        lines = target.read_text(encoding="utf-8", errors="replace").splitlines()
        blank = sum(not line.strip() for line in lines)
        longest = max((len(line) for line in lines), default=0)
        return (
            f"File: {target}\\n"
            f"Lines: {len(lines)}\\n"
            f"Blank: {blank}\\n"
            f"Longest: {longest} characters"
        )
        """,
    ),
    file_app(
        "csv_summary",
        "CSV Summary",
        "Summarize CSV rows, columns, and missing cells.",
        """
        target = path if path.is_file() else next(iter(sorted(path.rglob("*.csv"))), None)
        if target is None:
            return "No CSV file found. Pass a CSV path."
        with target.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.reader(handle))
        if not rows:
            return f"File: {target}\\nEmpty CSV."
        width = max(len(row) for row in rows)
        missing = sum(width - len(row) + sum(not cell.strip() for cell in row) for row in rows)
        return (
            f"File: {target}\\n"
            f"Data rows: {max(0, len(rows) - 1)}\\n"
            f"Columns: {width}\\n"
            f"Missing cells: {missing}"
        )
        """,
        ("import csv",),
    ),
    file_app(
        "csv_column_preview",
        "CSV Column Preview",
        "Show CSV headers and up to five example values per column.",
        """
        target = path if path.is_file() else next(iter(sorted(path.rglob("*.csv"))), None)
        if target is None:
            return "No CSV file found. Pass a CSV path."
        with target.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)[:5]
            headers = reader.fieldnames or []
        return "\\n".join(f"{header}: {', '.join(row.get(header, '') for row in rows)}" for header in headers) or "CSV has no headers."
        """,
        ("import csv",),
    ),
    file_app(
        "json_pretty_printer",
        "JSON Pretty Printer",
        "Validate and pretty-print a JSON file.",
        """
        target = path if path.is_file() else next(iter(sorted(path.rglob("*.json"))), None)
        if target is None:
            return "No JSON file found. Pass a JSON path."
        data = json.loads(target.read_text(encoding="utf-8"))
        return json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False)
        """,
        ("import json",),
    ),
    file_app(
        "json_key_finder",
        "JSON Key Finder",
        "List every dotted key path found in a JSON document.",
        """
        target = path if path.is_file() else next(iter(sorted(path.rglob("*.json"))), None)
        if target is None:
            return "No JSON file found. Pass a JSON path."
        data = json.loads(target.read_text(encoding="utf-8"))
        found: list[str] = []
        def walk(value: object, prefix: str = "") -> None:
            if isinstance(value, dict):
                for key, child in value.items():
                    current = f"{prefix}.{key}" if prefix else str(key)
                    found.append(current)
                    walk(child, current)
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    walk(child, f"{prefix}[{index}]")
        walk(data)
        return "\\n".join(found) or "No object keys found."
        """,
        ("import json",),
    ),
    file_app(
        "log_level_counter",
        "Log Level Counter",
        "Count common severity labels in a log file.",
        """
        target = path if path.is_file() else next((item for item in path.rglob("*.log") if item.is_file()), None)
        if target is None:
            return "No log file found. Pass a log path."
        content = target.read_text(encoding="utf-8", errors="replace")
        levels = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
        lines = []
        for level in levels:
            pattern = rf"\\b{level}\\b"
            count = len(re.findall(pattern, content, re.IGNORECASE))
            lines.append(f"{level}: {count}")
        return "\\n".join(lines)
        """,
        ("import re",),
    ),
    file_app(
        "ini_inspector",
        "INI Inspector",
        "List sections and keys in an INI configuration file.",
        """
        target = path if path.is_file() else next(iter(sorted(path.rglob("*.ini"))), None)
        if target is None:
            return "No INI file found. Pass an INI path."
        parser = configparser.ConfigParser()
        parser.read(target, encoding="utf-8")
        lines = [f"[{section}]\\n" + "\\n".join(f"  {key}" for key in parser[section]) for section in parser.sections()]
        return "\\n".join(lines) or "No sections found."
        """,
        ("import configparser",),
    ),
    file_app(
        "recent_file_report",
        "Recent File Report",
        "List recently modified files below a path.",
        """
        files = [path] if path.is_file() else [item for item in path.rglob("*") if item.is_file()]
        newest = sorted(files, key=lambda item: item.stat().st_mtime, reverse=True)[:20]
        lines = []
        for item in newest:
            modified = datetime.fromtimestamp(item.stat().st_mtime, tz=UTC)
            lines.append(f"{modified.isoformat()}  {item}")
        return "\\n".join(lines) or "No files found."
        """,
        ("from datetime import UTC, datetime",),
    ),
    file_app(
        "largest_file_report",
        "Largest File Report",
        "List the largest files beneath a path.",
        """
        files = [path] if path.is_file() else [item for item in path.rglob("*") if item.is_file()]
        largest = sorted(files, key=lambda item: item.stat().st_size, reverse=True)[:20]
        return "\\n".join(f"{item.stat().st_size:>12,}  {item}" for item in largest) or "No files found."
        """,
    ),
    file_app(
        "empty_file_finder",
        "Empty File Finder",
        "Find zero-byte files and empty directories without deleting them.",
        """
        if path.is_file():
            return str(path) if path.stat().st_size == 0 else "File is not empty."
        empty_files = [item for item in path.rglob("*") if item.is_file() and item.stat().st_size == 0]
        empty_dirs = [item for item in path.rglob("*") if item.is_dir() and not any(item.iterdir())]
        lines = [*(f"FILE {item}" for item in empty_files), *(f"DIR  {item}" for item in empty_dirs)]
        return "\\n".join(lines) or "No empty files or directories found."
        """,
    ),
    file_app(
        "filename_sanitizer_preview",
        "Filename Sanitizer Preview",
        "Preview portable sanitized filenames without renaming anything.",
        """
        entries = [path] if path.is_file() else sorted(path.iterdir())
        lines = []
        for item in entries:
            cleaned_stem = re.sub(r"[^A-Za-z0-9._-]+", "_", item.stem).strip("._") or "unnamed"
            cleaned = cleaned_stem + item.suffix.casefold()
            if item.name != cleaned:
                lines.append(f"{item.name} -> {cleaned}")
        return "\\n".join(lines) or "No filename changes suggested."
        """,
        ("import re",),
    ),
    file_app(
        "batch_rename_preview",
        "Batch Rename Preview",
        "Preview sequential filenames for files in a directory.",
        """
        if path.is_file():
            return f"001_{path.name}"
        files = sorted((item for item in path.iterdir() if item.is_file()), key=lambda item: item.name.casefold())
        width = max(3, len(str(len(files))))
        return "\\n".join(f"{item.name} -> {index:0{width}d}_{item.name}" for index, item in enumerate(files, 1)) or "No files found."
        """,
    ),
    file_app(
        "text_encoding_probe",
        "Text Encoding Probe",
        "Check whether a file decodes as UTF-8, UTF-8 with BOM, or Latin-1.",
        """
        target = path if path.is_file() else next((item for item in path.rglob("*") if item.is_file()), None)
        if target is None:
            return "No file found."
        data = target.read_bytes()
        for encoding in ("utf-8-sig", "utf-8", "latin-1"):
            try:
                decoded = data.decode(encoding)
            except UnicodeDecodeError:
                continue
            replacement_count = decoded.count("�")
            return (
                f"File: {target}\\n"
                f"Compatible encoding: {encoding}\\n"
                f"Characters: {len(decoded)}\\n"
                f"Replacement characters: {replacement_count}"
            )
        return "No tested encoding succeeded."
        """,
    ),
    file_app(
        "todo_scanner",
        "TODO Scanner",
        "Find TODO, FIXME, and NOTE markers in text files.",
        """
        files = [path] if path.is_file() else [item for item in path.rglob("*") if item.is_file() and item.suffix.casefold() in {".py", ".md", ".txt", ".js", ".ts"}]
        matches: list[str] = []
        pattern = re.compile(r"\\b(TODO|FIXME|NOTE)\\b", re.IGNORECASE)
        for item in files:
            for number, line in enumerate(item.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                if pattern.search(line):
                    matches.append(f"{item}:{number}: {line.strip()}")
        return "\\n".join(matches[:200]) or "No markers found."
        """,
        ("import re",),
    ),
    file_app(
        "python_import_scanner",
        "Python Import Scanner",
        "List imported top-level modules from Python source files using the AST.",
        """
        files = [path] if path.is_file() else list(path.rglob("*.py"))
        imports: Counter[str] = Counter()
        for item in files:
            tree = ast.parse(item.read_text(encoding="utf-8"), filename=str(item))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imports.update(alias.name.split(".")[0] for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imports.update([node.module.split(".")[0]])
        return "\\n".join(f"{name}: {count}" for name, count in imports.most_common()) or "No imports found."
        """,
        ("import ast", "from collections import Counter"),
    ),
)


def game(
    slug: str,
    title: str,
    summary: str,
    body: str,
    imports: tuple[str, ...] = (),
) -> GameApp:
    """Build terminal game specification."""
    return GameApp("games", slug, title, summary, body, imports)


GAMES: tuple[AppSpec, ...] = (
    game(
        "number_guess",
        "Number Guess",
        "Guess a hidden number from 1 to 100 with higher-or-lower clues.",
        """
        rng = random.Random(seed)
        target = rng.randint(1, 100)
        if not interactive:
            guesses = [50, 75, target]
            clues = ["correct" if guess == target else ("higher" if guess < target else "lower") for guess in guesses]
            return "Demo target: " + str(target) + "\\n" + "\\n".join(f"Guess {guess}: {clue}" for guess, clue in zip(guesses, clues, strict=True))
        for attempt in range(1, 11):
            guess = int(input(f"Attempt {attempt}/10 — number: "))
            if guess == target:
                return f"Correct in {attempt} attempts!"
            print("Higher." if guess < target else "Lower.")
        return f"Out of attempts. Answer: {target}"
        """,
    ),
    game(
        "rock_paper_scissors",
        "Rock Paper Scissors",
        "Play one classic hand-game round against the computer.",
        """
        rng = random.Random(seed)
        choices = ("rock", "paper", "scissors")
        computer = rng.choice(choices)
        player = input("rock, paper, or scissors? ").strip().casefold() if interactive else "rock"
        if player not in choices:
            return "Invalid choice."
        wins = {("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")}
        outcome = "draw" if player == computer else ("win" if (player, computer) in wins else "lose")
        return f"You: {player}\\nComputer: {computer}\\nResult: {outcome}"
        """,
    ),
    game(
        "dice_duel",
        "Dice Duel",
        "Roll two dice against a computer opponent for three rounds.",
        """
        rng = random.Random(seed)
        player_score = 0
        computer_score = 0
        lines = []
        for round_number in range(1, 4):
            if interactive:
                input(f"Press Enter to roll round {round_number}.")
            player_roll = rng.randint(1, 6) + rng.randint(1, 6)
            computer_roll = rng.randint(1, 6) + rng.randint(1, 6)
            player_score += player_roll > computer_roll
            computer_score += computer_roll > player_roll
            lines.append(f"Round {round_number}: you {player_roll}, computer {computer_roll}")
        winner = "you" if player_score > computer_score else ("computer" if computer_score > player_score else "draw")
        return "\\n".join((*lines, f"Winner: {winner}"))
        """,
    ),
    game(
        "higher_lower",
        "Higher or Lower",
        "Predict whether a second card will be higher than the first.",
        """
        rng = random.Random(seed)
        first, second = rng.sample(range(1, 14), 2)
        choice = input("Will next card be higher or lower? ").strip().casefold() if interactive else "higher"
        actual = "higher" if second > first else "lower"
        result = "Correct!" if choice == actual else f"No, it was {actual}."
        return (
            f"First: {first}\\n"
            f"Second: {second}\\n"
            f"Your choice: {choice}\\n"
            f"{result}"
        )
        """,
    ),
    game(
        "word_scramble",
        "Word Scramble",
        "Unscramble a shuffled Python-related word.",
        """
        rng = random.Random(seed)
        word = rng.choice(("iterator", "function", "variable", "package", "terminal"))
        letters = list(word)
        rng.shuffle(letters)
        scrambled = "".join(letters)
        if not interactive:
            return f"Scrambled: {scrambled}\\nAnswer: {word}"
        guess = input(f"Unscramble {scrambled}: ").strip().casefold()
        return "Correct!" if guess == word else f"Answer: {word}"
        """,
    ),
    game(
        "hangman_lite",
        "Hangman Lite",
        "Guess letters in a short word before six misses.",
        """
        rng = random.Random(seed)
        word = rng.choice(("planet", "bridge", "python", "garden"))
        if not interactive:
            return f"Puzzle: {' '.join('_' for _ in word)}\\nDemo answer: {word}"
        guessed: set[str] = set()
        misses = 0
        while misses < 6 and any(letter not in guessed for letter in word):
            print(" ".join(letter if letter in guessed else "_" for letter in word))
            letter = input("Letter: ").strip().casefold()[:1]
            if letter in guessed:
                continue
            guessed.add(letter)
            if letter not in word:
                misses += 1
        result = "Won" if all(letter in guessed for letter in word) else "Lost"
        return f"{result}! Word: {word}"
        """,
    ),
    game(
        "nim_stones",
        "Nim Stones",
        "Take one to three stones; player taking the last stone wins.",
        """
        rng = random.Random(seed)
        stones = 15
        lines = []
        while stones > 0:
            if interactive:
                take = int(input(f"{stones} stones. Take 1-3: "))
                if take not in {1, 2, 3} or take > stones:
                    return "Invalid move."
            else:
                take = rng.randint(1, min(3, stones))
            stones -= take
            lines.append(f"Player takes {take}; {stones} remain")
            if stones == 0:
                return "\\n".join((*lines, "Player wins!"))
            computer = min(stones, 4 - take)
            stones -= computer
            lines.append(f"Computer takes {computer}; {stones} remain")
            if stones == 0:
                return "\\n".join((*lines, "Computer wins!"))
        return "\\n".join(lines)
        """,
    ),
    game(
        "codebreaker",
        "Codebreaker",
        "Crack a four-digit code using exact and misplaced digit clues.",
        """
        rng = random.Random(seed)
        code = "".join(str(rng.randrange(10)) for _ in range(4))
        if not interactive:
            guess = "1234"
            exact = sum(left == right for left, right in zip(code, guess, strict=True))
            return f"Guess {guess}: {exact} exact\\nDemo code: {code}"
        for turn in range(1, 9):
            guess = input(f"Turn {turn}/8, four digits: ").strip()
            if len(guess) != 4 or not guess.isdigit():
                return "Invalid code format."
            exact = sum(left == right for left, right in zip(code, guess, strict=True))
            misplaced = sum((Counter(code) & Counter(guess)).values()) - exact
            if exact == 4:
                return f"Cracked in {turn} turns!"
            print(f"Exact: {exact}; misplaced: {misplaced}")
        return f"Code was {code}."
        """,
        ("from collections import Counter",),
    ),
    game(
        "math_race",
        "Math Race",
        "Solve five generated arithmetic questions against a timer-free score target.",
        """
        rng = random.Random(seed)
        questions = [(rng.randint(2, 12), rng.randint(2, 12)) for _ in range(5)]
        if not interactive:
            return "\\n".join(f"{left} × {right} = {left * right}" for left, right in questions)
        score = 0
        for left, right in questions:
            answer = int(input(f"{left} × {right} = "))
            score += answer == left * right
        return f"Score: {score}/{len(questions)}"
        """,
    ),
    game(
        "trivia_challenge",
        "Trivia Challenge",
        "Answer a shuffled set of general-knowledge questions.",
        """
        rng = random.Random(seed)
        questions = [("Largest ocean?", "pacific"), ("How many sides in a hexagon?", "6"), ("Planet known as the Red Planet?", "mars")]
        rng.shuffle(questions)
        if not interactive:
            return "\\n".join(f"{question} {answer.title()}" for question, answer in questions)
        score = sum(input(f"{question} ").strip().casefold() == answer for question, answer in questions)
        return f"Score: {score}/{len(questions)}"
        """,
    ),
    game(
        "blackjack_lite",
        "Blackjack Lite",
        "Play a simplified hit-or-stand blackjack hand.",
        """
        rng = random.Random(seed)
        deck = [min(rank, 10) for rank in range(1, 14) for _ in range(4)]
        rng.shuffle(deck)
        player = [deck.pop(), deck.pop()]
        dealer = [deck.pop(), deck.pop()]
        while sum(player) < 21 and interactive and input(f"Hand {player} ({sum(player)}). Hit? [y/N] ").casefold() == "y":
            player.append(deck.pop())
        while sum(dealer) < 17:
            dealer.append(deck.pop())
        player_total, dealer_total = sum(player), sum(dealer)
        if player_total > 21:
            result = "bust"
        elif dealer_total > 21 or player_total > dealer_total:
            result = "win"
        elif player_total == dealer_total:
            result = "push"
        else:
            result = "lose"
        return (
            f"Your hand: {player} = {player_total}\\n"
            f"Dealer: {dealer} = {dealer_total}\\n"
            f"Result: {result}"
        )
        """,
    ),
    game(
        "coin_streak",
        "Coin Streak Hunt",
        "Flip coins until a target run of matching sides appears.",
        """
        rng = random.Random(seed)
        target = 4
        previous = ""
        streak = 0
        flips: list[str] = []
        while streak < target:
            if interactive:
                input("Press Enter to flip.")
            current = rng.choice(("H", "T"))
            flips.append(current)
            streak = streak + 1 if current == previous else 1
            previous = current
        return (
            f"Flips: {' '.join(flips)}\\n"
            f"Found {target} {previous} in a row after {len(flips)} flips."
        )
        """,
    ),
    game(
        "memory_sequence",
        "Memory Sequence",
        "Memorize and repeat an expanding digit sequence.",
        """
        rng = random.Random(seed)
        sequence = "".join(str(rng.randrange(10)) for _ in range(6))
        if not interactive:
            return f"Study: {sequence}\\nCover it and type it from memory."
        print(f"Memorize: {sequence}")
        input("Press Enter when ready.")
        print("\\n" * 20)
        guess = input("Sequence: ").strip()
        return "Perfect memory!" if guess == sequence else f"Answer: {sequence}"
        """,
    ),
    game(
        "tic_tac_toe",
        "Tic-Tac-Toe",
        "Play a compact tic-tac-toe match against random moves.",
        """
        rng = random.Random(seed)
        board = [" "] * 9
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        turn = "X"
        while " " in board and not any(board[a] == board[b] == board[c] != " " for a, b, c in wins):
            available = [index for index, value in enumerate(board) if value == " "]
            if interactive and turn == "X":
                move = int(input(f"Cells 1-9, available {[index + 1 for index in available]}: ")) - 1
                if move not in available:
                    return "Invalid move."
            else:
                move = rng.choice(available)
            board[move] = turn
            turn = "O" if turn == "X" else "X"
        rows = [" | ".join(board[index:index + 3]) for index in range(0, 9, 3)]
        winner = next((board[a] for a, b, c in wins if board[a] == board[b] == board[c] != " "), "draw")
        return "\\n---------\\n".join(rows) + f"\\nWinner: {winner}"
        """,
    ),
    game(
        "minesweeper_lite",
        "Minesweeper Lite",
        "Reveal one cell on a generated five-by-five minefield.",
        """
        rng = random.Random(seed)
        mines = set(rng.sample(range(25), 5))
        if interactive:
            row = int(input("Row 1-5: ")) - 1
            column = int(input("Column 1-5: ")) - 1
        else:
            row, column = 2, 2
        index = row * 5 + column
        if row not in range(5) or column not in range(5):
            return "Cell outside board."
        if index in mines:
            return f"Cell {row + 1},{column + 1}: mine!"
        neighbors = sum((near_row * 5 + near_column) in mines for near_row in range(max(0, row - 1), min(5, row + 2)) for near_column in range(max(0, column - 1), min(5, column + 2)))
        return f"Cell {row + 1},{column + 1}: {neighbors} neighboring mines."
        """,
    ),
    game(
        "maze_path",
        "Maze Path",
        "Navigate a small generated obstacle grid toward a goal.",
        """
        rng = random.Random(seed)
        size = 7
        blocked = set(rng.sample(list(range(1, size * size - 1)), 10))
        blocked -= {1, size}
        position = 0
        moves = input("Moves using UDLR: ").strip().upper() if interactive else "RRDDRRDDRRDD"
        for move in moves:
            row, column = divmod(position, size)
            candidate = {"U": (row - 1, column), "D": (row + 1, column), "L": (row, column - 1), "R": (row, column + 1)}.get(move, (row, column))
            next_row, next_column = candidate
            next_position = next_row * size + next_column
            if 0 <= next_row < size and 0 <= next_column < size and next_position not in blocked:
                position = next_position
        grid = ["#" if index in blocked else ("P" if index == position else ("G" if index == size * size - 1 else ".")) for index in range(size * size)]
        return "\\n".join("".join(grid[row * size:(row + 1) * size]) for row in range(size))
        """,
    ),
    game(
        "tiny_adventure",
        "Tiny Adventure",
        "Choose a path through a three-scene text adventure.",
        """
        rng = random.Random(seed)
        first = input("Forest or river? ").strip().casefold() if interactive else rng.choice(("forest", "river"))
        if first == "forest":
            second = input("Climb or listen? ").strip().casefold() if interactive else "listen"
            ending = "You hear the hidden village invite you in." if second == "listen" else "The old tree shows a road in its rings."
        elif first == "river":
            second = input("Boat or bridge? ").strip().casefold() if interactive else "bridge"
            ending = "The bridge wakes and asks one excellent riddle." if second == "bridge" else "The boat carries you to tomorrow morning."
        else:
            return "Unknown path."
        return f"Path: {first} -> {second}\\n{ending}"
        """,
    ),
    game(
        "word_ladder",
        "Word Ladder",
        "Change one letter at a time to transform one word into another.",
        """
        rng = random.Random(seed)
        ladders = (("cold", "cord", "card", "ward", "warm"), ("head", "heal", "teal", "tell", "tall", "tail"))
        ladder = rng.choice(ladders)
        if not interactive:
            return f"Puzzle: {ladder[0]} -> {ladder[-1]}\\nOne answer: {' -> '.join(ladder)}"
        response = input(f"Enter comma-separated ladder from {ladder[0]} to {ladder[-1]}: ").casefold().split(",")
        words = [word.strip() for word in response]
        valid = words[0] == ladder[0] and words[-1] == ladder[-1] and all(sum(a != b for a, b in zip(left, right, strict=True)) == 1 for left, right in itertools.pairwise(words))
        return "Valid ladder!" if valid else f"Example: {' -> '.join(ladder)}"
        """,
        ("import itertools",),
    ),
    game(
        "sliding_tiles",
        "Sliding Tiles",
        "Apply one move to a tiny 2×2 sliding-tile puzzle.",
        """
        rng = random.Random(seed)
        board = [1, 2, 3, 0]
        for _ in range(10):
            zero = board.index(0)
            row, column = divmod(zero, 2)
            neighbors = [candidate for candidate in range(4) if abs(divmod(candidate, 2)[0] - row) + abs(divmod(candidate, 2)[1] - column) == 1]
            swap = rng.choice(neighbors)
            board[zero], board[swap] = board[swap], board[zero]
        before = board.copy()
        if interactive:
            tile = int(input(f"Board {before}; tile to slide: "))
        else:
            zero = board.index(0)
            tile = board[next(candidate for candidate in range(4) if board[candidate] and abs(divmod(candidate, 2)[0] - divmod(zero, 2)[0]) + abs(divmod(candidate, 2)[1] - divmod(zero, 2)[1]) == 1)]
        tile_index, zero_index = board.index(tile), board.index(0)
        adjacent = abs(divmod(tile_index, 2)[0] - divmod(zero_index, 2)[0]) + abs(divmod(tile_index, 2)[1] - divmod(zero_index, 2)[1]) == 1
        if adjacent:
            board[tile_index], board[zero_index] = board[zero_index], board[tile_index]
        return f"Before: {before}\\nAfter:  {board}\\nMove valid: {adjacent}"
        """,
    ),
    game(
        "battleship_shot",
        "Battleship Shot",
        "Fire one shot at a hidden ship on a five-by-five grid.",
        """
        rng = random.Random(seed)
        horizontal = rng.choice((True, False))
        start_row = rng.randrange(5 if horizontal else 3)
        start_column = rng.randrange(3 if horizontal else 5)
        ship = {(start_row + (0 if horizontal else offset), start_column + (offset if horizontal else 0)) for offset in range(3)}
        if interactive:
            shot = (int(input("Row 1-5: ")) - 1, int(input("Column 1-5: ")) - 1)
        else:
            shot = (2, 2)
        result = "hit" if shot in ship else "miss"
        visible_ship = sorted((row + 1, column + 1) for row, column in ship)
        return (
            f"Shot {shot[0] + 1},{shot[1] + 1}: {result}.\\n"
            f"Demo ship cells: {visible_ship}"
        )
        """,
    ),
)


ALL_APPS: tuple[AppSpec, ...] = (
    *CALCULATORS,
    *TEXT_TOOLS,
    *FILE_TOOLS,
    *LEARNING,
    *CREATIVE,
    *GAMES,
    *PLANNING,
    *DEVELOPER,
)
