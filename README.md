# Python Scripts V2

Curated collection of **162 standalone Python 3 apps**. Every app has one Python file, its own README, and its own `requirements.txt`. Categories balance useful utilities, learning exercises, creative prompts, and playable terminal games.

## Quick start

```bash
python3 apps/calculators/tip_calculator/tip_calculator.py
python3 apps/games/number_guess/number_guess.py --play
```

No app needs third-party runtime packages. Each defaults to a safe, noninteractive demo. Filesystem tools are read-only.

## Development

```bash
uv sync
make verify
```

Quality gates use Ruff with every rule family enabled, narrow documented exclusions, strict mypy, structural contract checks, and one smoke-test case per app.

## Repository layout

```text
apps/<category>/<app>/<app>.py
apps/<category>/<app>/README.md
apps/<category>/<app>/requirements.txt
tests/test_catalog.py
tools/build_catalog.py
catalog.json
```

`catalog.json` is the machine-readable index. Regenerate and format checked-in app files and docs with `make catalog`.

## App catalog

## Calculators

- [Age in Days Estimator](apps/calculators/age_in_days/README.md) — Estimate age in days and hours from years.
- [BMI Calculator](apps/calculators/bmi_calculator/README.md) — Calculate body mass index from metric measurements.
- [Break-even Calculator](apps/calculators/break_even/README.md) — Find sales volume needed to cover fixed costs.
- [Compound Interest Calculator](apps/calculators/compound_interest/README.md) — Estimate investment growth with monthly compounding.
- [Data Size Converter](apps/calculators/data_size_converter/README.md) — Convert bytes into binary storage units.
- [Electricity Cost Calculator](apps/calculators/electricity_cost/README.md) — Estimate appliance energy use and cost.
- [Fuel Cost Calculator](apps/calculators/fuel_cost/README.md) — Estimate fuel volume and trip cost.
- [Weighted Grade Calculator](apps/calculators/grade_average/README.md) — Combine two assessment scores using configurable weights.
- [Length Converter](apps/calculators/length_converter/README.md) — Convert meters into common metric and imperial lengths.
- [Loan Payment Calculator](apps/calculators/loan_payment/README.md) — Estimate monthly payment and total loan cost.
- [Paint Estimator](apps/calculators/paint_estimator/README.md) — Estimate paint needed for rectangular walls.
- [Percentage Change Calculator](apps/calculators/percentage_change/README.md) — Measure absolute and percentage change between values.
- [Recipe Scaler](apps/calculators/recipe_scaler/README.md) — Scale an ingredient amount between serving counts.
- [Running Pace Calculator](apps/calculators/running_pace/README.md) — Convert race distance and finish time into running pace.
- [Savings Goal Calculator](apps/calculators/savings_goal/README.md) — Estimate months needed to reach a savings target.
- [Screen PPI Calculator](apps/calculators/screen_ppi/README.md) — Calculate display pixel density from resolution and diagonal size.
- [Temperature Converter](apps/calculators/temperature_converter/README.md) — Convert Celsius into Fahrenheit and Kelvin.
- [Time Zone Offset Calculator](apps/calculators/time_zone_offset/README.md) — Shift a 24-hour clock time by a UTC offset.
- [Tip Calculator](apps/calculators/tip_calculator/README.md) — Split a restaurant bill with a configurable tip.
- [Unit Price Comparator](apps/calculators/unit_price_comparator/README.md) — Compare two package prices using cost per unit.

## Creative

- [ASCII Pattern Designer](apps/creative/ascii_pattern/README.md) — Generate small instructions for text-based geometric art.
- [Character Builder](apps/creative/character_builder/README.md) — Create compact character concepts with motivations and contradictions.
- [Chord Progression Generator](apps/creative/chord_progression/README.md) — Suggest song sections using Roman-numeral chord progressions.
- [Color Palette Namer](apps/creative/color_palette/README.md) — Invent themed color-palette briefs for visual projects.
- [Comic Panel Generator](apps/creative/comic_panel/README.md) — Create three-beat visual comedy setups for drawing practice.
- [Dungeon Room Generator](apps/creative/dungeon_room/README.md) — Build tabletop dungeon rooms with hazards, clues, and rewards.
- [Fantasy Name Generator](apps/creative/fantasy_name/README.md) — Generate pronounceable fantasy place and character names.
- [Haiku Seed Generator](apps/creative/haiku_seed/README.md) — Offer three vivid image fragments for drafting a haiku.
- [Logo Brief Generator](apps/creative/logo_brief/README.md) — Draft compact fictional logo briefs for design practice.
- [Melody Pattern Generator](apps/creative/melody_pattern/README.md) — Create scale-degree motifs for melody practice.
- [Metaphor Mixer](apps/creative/metaphor_mixer/README.md) — Mix sensory images into surprising metaphor starters.
- [NPC Dialogue Seed](apps/creative/npc_dialogue/README.md) — Generate tabletop NPC voices, needs, and opening lines.
- [Planet Generator](apps/creative/planet_generator/README.md) — Invent science-fiction worlds with environments and mysteries.
- [Plot Twist Generator](apps/creative/plot_twist/README.md) — Add fair but surprising reversals to story outlines.
- [Poem Seed Generator](apps/creative/poem_seed/README.md) — Offer a title, image, sound, and final-word constraint for a poem.
- [Recipe Idea Generator](apps/creative/recipe_idea/README.md) — Combine ingredients, techniques, and flavor directions for cooking experiments.
- [Story Prompt Generator](apps/creative/story_prompt/README.md) — Combine a protagonist, goal, obstacle, and setting into writing prompts.
- [Superhero Generator](apps/creative/superhero_generator/README.md) — Create unusual heroes with powers, limits, and civic problems.
- [Worldbuilding Question Generator](apps/creative/worldbuilding_question/README.md) — Ask focused questions that expose consequences in fictional worlds.
- [Writing Constraint Generator](apps/creative/writing_constraint/README.md) — Create playful constraints for a short writing exercise.

## Developer

- [Base64 Encoder](apps/developer/base64_encoder/README.md) — Encode UTF-8 text as Base64.
- [Chmod Calculator](apps/developer/chmod_calculator/README.md) — Convert a three-digit Unix permission mode into symbolic form.
- [Color Converter](apps/developer/color_converter/README.md) — Convert a six-digit hexadecimal color to RGB and HSL.
- [Cron Field Explainer](apps/developer/cron_explainer/README.md) — Explain the five fields of a basic cron expression.
- [Deterministic UUID](apps/developer/deterministic_uuid/README.md) — Create a stable UUID from a text namespace value.
- [Environment Diff](apps/developer/env_diff/README.md) — Compare KEY=VALUE blocks separated by a vertical bar without changing files.
- [Fake Record Generator](apps/developer/fake_record_generator/README.md) — Create deterministic fictional test data from a seed phrase.
- [Text Hashes](apps/developer/hash_text/README.md) — Calculate SHA-256 and SHA-512 digests for text.
- [HTTP Status Lookup](apps/developer/http_status_lookup/README.md) — Look up the standard phrase for an HTTP status code.
- [JWT Payload Decoder](apps/developer/jwt_payload_decoder/README.md) — Decode a JWT payload locally without claiming signature verification.
- [Lorem Generator](apps/developer/lorem_generator/README.md) — Generate a deterministic filler paragraph from a numeric word count.
- [Markdown Table Maker](apps/developer/markdown_table_maker/README.md) — Convert semicolon-separated rows and comma-separated cells into a Markdown table.
- [Query String Parser](apps/developer/query_string_parser/README.md) — Parse a URL query string into readable key-value pairs.
- [Regex Tester](apps/developer/regex_tester/README.md) — Test a regular expression against text separated by a vertical bar.
- [Semantic Version Compare](apps/developer/semantic_version_compare/README.md) — Compare two numeric semantic versions separated by a vertical bar.
- [SQL Keyword Formatter](apps/developer/sql_keyword_formatter/README.md) — Uppercase common SQL keywords and place major clauses on new lines.
- [Subnet Inspector](apps/developer/subnet_inspector/README.md) — Inspect an IPv4 or IPv6 network in CIDR notation.
- [Text to Hex](apps/developer/text_to_hex/README.md) — Show UTF-8 bytes as hexadecimal and decimal values.
- [Unified Diff Maker](apps/developer/unified_diff/README.md) — Compare two short text blocks separated by a vertical bar.
- [Unix Timestamp Converter](apps/developer/unix_timestamp/README.md) — Convert an ISO-8601 datetime into a Unix timestamp.
- [URL Encoder](apps/developer/url_encoder/README.md) — Percent-encode text for safe URL query use.

## File Tools

- [Batch Rename Preview](apps/file_tools/batch_rename_preview/README.md) — Preview sequential filenames for files in a directory.
- [Checksum Maker](apps/file_tools/checksum_maker/README.md) — Calculate SHA-256 checksums for a file or directory.
- [CSV Column Preview](apps/file_tools/csv_column_preview/README.md) — Show CSV headers and up to five example values per column.
- [CSV Summary](apps/file_tools/csv_summary/README.md) — Summarize CSV rows, columns, and missing cells.
- [Directory Tree](apps/file_tools/directory_tree/README.md) — Print a compact, sorted directory tree.
- [Disk Usage Report](apps/file_tools/disk_usage_report/README.md) — Summarize file counts and byte usage beneath a path.
- [Duplicate File Finder](apps/file_tools/duplicate_file_finder/README.md) — Find exact duplicate files using size and SHA-256 without deleting anything.
- [Empty File Finder](apps/file_tools/empty_file_finder/README.md) — Find zero-byte files and empty directories without deleting them.
- [File Extension Counter](apps/file_tools/extension_counter/README.md) — Count files by extension beneath a directory.
- [Filename Sanitizer Preview](apps/file_tools/filename_sanitizer_preview/README.md) — Preview portable sanitized filenames without renaming anything.
- [INI Inspector](apps/file_tools/ini_inspector/README.md) — List sections and keys in an INI configuration file.
- [JSON Key Finder](apps/file_tools/json_key_finder/README.md) — List every dotted key path found in a JSON document.
- [JSON Pretty Printer](apps/file_tools/json_pretty_printer/README.md) — Validate and pretty-print a JSON file.
- [Largest File Report](apps/file_tools/largest_file_report/README.md) — List the largest files beneath a path.
- [Line Statistics](apps/file_tools/line_statistics/README.md) — Count text lines, blank lines, and longest line length.
- [Log Level Counter](apps/file_tools/log_level_counter/README.md) — Count common severity labels in a log file.
- [Python Import Scanner](apps/file_tools/python_import_scanner/README.md) — List imported top-level modules from Python source files using the AST.
- [Recent File Report](apps/file_tools/recent_file_report/README.md) — List recently modified files below a path.
- [Text Encoding Probe](apps/file_tools/text_encoding_probe/README.md) — Check whether a file decodes as UTF-8, UTF-8 with BOM, or Latin-1.
- [TODO Scanner](apps/file_tools/todo_scanner/README.md) — Find TODO, FIXME, and NOTE markers in text files.

## Games

- [Battleship Shot](apps/games/battleship_shot/README.md) — Fire one shot at a hidden ship on a five-by-five grid.
- [Blackjack Lite](apps/games/blackjack_lite/README.md) — Play a simplified hit-or-stand blackjack hand.
- [Codebreaker](apps/games/codebreaker/README.md) — Crack a four-digit code using exact and misplaced digit clues.
- [Coin Streak Hunt](apps/games/coin_streak/README.md) — Flip coins until a target run of matching sides appears.
- [Dice Duel](apps/games/dice_duel/README.md) — Roll two dice against a computer opponent for three rounds.
- [Hangman Lite](apps/games/hangman_lite/README.md) — Guess letters in a short word before six misses.
- [Higher or Lower](apps/games/higher_lower/README.md) — Predict whether a second card will be higher than the first.
- [Math Race](apps/games/math_race/README.md) — Solve five generated arithmetic questions against a timer-free score target.
- [Maze Path](apps/games/maze_path/README.md) — Navigate a small generated obstacle grid toward a goal.
- [Memory Sequence](apps/games/memory_sequence/README.md) — Memorize and repeat an expanding digit sequence.
- [Minesweeper Lite](apps/games/minesweeper_lite/README.md) — Reveal one cell on a generated five-by-five minefield.
- [Nim Stones](apps/games/nim_stones/README.md) — Take one to three stones; player taking the last stone wins.
- [Number Guess](apps/games/number_guess/README.md) — Guess a hidden number from 1 to 100 with higher-or-lower clues.
- [Rock Paper Scissors](apps/games/rock_paper_scissors/README.md) — Play one classic hand-game round against the computer.
- [Sliding Tiles](apps/games/sliding_tiles/README.md) — Apply one move to a tiny 2×2 sliding-tile puzzle.
- [Tic-Tac-Toe](apps/games/tic_tac_toe/README.md) — Play a compact tic-tac-toe match against random moves.
- [Tiny Adventure](apps/games/tiny_adventure/README.md) — Choose a path through a three-scene text adventure.
- [Trivia Challenge](apps/games/trivia_challenge/README.md) — Answer a shuffled set of general-knowledge questions.
- [Word Ladder](apps/games/word_ladder/README.md) — Change one letter at a time to transform one word into another.
- [Word Scramble](apps/games/word_scramble/README.md) — Unscramble a shuffled Python-related word.

## Learning

- [Art History Quiz](apps/learning/art_history/README.md) — Connect major art movements with defining ideas.
- [Astronomy Basics Quiz](apps/learning/astronomy_basics/README.md) — Review solar-system and stellar concepts.
- [Binary Number Quiz](apps/learning/binary_numbers/README.md) — Practice converting small binary and decimal values.
- [Capital City Quiz](apps/learning/capital_cities/README.md) — Practice country and capital pairs.
- [Computer Networks Quiz](apps/learning/computer_networks/README.md) — Review practical networking concepts and protocols.
- [Electricity Basics Quiz](apps/learning/electricity_basics/README.md) — Review voltage, current, resistance, and power.
- [Fraction Skills Quiz](apps/learning/fraction_skills/README.md) — Practice simplifying and comparing fractions.
- [Geology Basics Quiz](apps/learning/geology_basics/README.md) — Learn rock types and Earth structure.
- [Human Body Quiz](apps/learning/human_body/README.md) — Review foundational anatomy and physiology.
- [Logical Reasoning Quiz](apps/learning/logical_reasoning/README.md) — Practice basic logical operators and implications.
- [Multiplication Trainer](apps/learning/multiplication_trainer/README.md) — Practice mental multiplication facts.
- [Music Theory Quiz](apps/learning/music_theory/README.md) — Review intervals, scales, and notation.
- [Periodic Table Quiz](apps/learning/periodic_table/README.md) — Review common chemical element symbols.
- [Physics Motion Quiz](apps/learning/physics_motion/README.md) — Review basic speed, acceleration, and force ideas.
- [Prime Number Quiz](apps/learning/prime_numbers/README.md) — Review factors and small prime numbers.
- [Probability Basics Quiz](apps/learning/probability_basics/README.md) — Practice simple event probabilities.
- [Python Basics Quiz](apps/learning/python_basics/README.md) — Review core Python syntax and data types.
- [Statistics Basics Quiz](apps/learning/statistics_basics/README.md) — Review mean, median, mode, and range.
- [Vocabulary Builder](apps/learning/vocabulary_builder/README.md) — Learn precise English vocabulary through short definitions.
- [World History Quiz](apps/learning/world_history/README.md) — Review selected milestones from world history.

## Planning

- [Battery Runtime Estimator](apps/planning/battery_runtime/README.md) — Estimate ideal battery runtime from capacity and device draw.
- [50-30-20 Budget Allocator](apps/planning/budget_allocator/README.md) — Split take-home income into needs, wants, and savings targets.
- [Commute Emissions Estimator](apps/planning/commute_emissions/README.md) — Estimate travel emissions using a configurable per-kilometer factor.
- [Commute Time Planner](apps/planning/commute_time/README.md) — Estimate weekly and annual commute time.
- [Debt Payoff Estimator](apps/planning/debt_payoff/README.md) — Estimate payoff time without interest using a fixed monthly payment.
- [Emergency Fund Planner](apps/planning/emergency_fund/README.md) — Estimate emergency-fund target and funding time.
- [Event Capacity Planner](apps/planning/event_capacity/README.md) — Estimate table count and floor-space needs for an event.
- [Freelance Rate Planner](apps/planning/freelance_rate/README.md) — Estimate an hourly freelance rate from income and overhead goals.
- [Garden Spacing Planner](apps/planning/garden_spacing/README.md) — Estimate plant capacity for a rectangular garden bed.
- [Hydration Goal](apps/planning/hydration_goal/README.md) — Estimate a simple daily water goal from body weight and activity.
- [Meal Portion Planner](apps/planning/meal_portion/README.md) — Scale meal portions across people and meals.
- [Meeting Cost Estimator](apps/planning/meeting_cost/README.md) — Estimate labor cost of a meeting.
- [Pet Food Planner](apps/planning/pet_food_plan/README.md) — Estimate food needed and cost over a planning period.
- [Pomodoro Plan](apps/planning/pomodoro_plan/README.md) — Turn work and break intervals into a session timeline.
- [Reading Plan](apps/planning/reading_plan/README.md) — Estimate daily pages and reading time for a deadline.
- [Retirement Contribution Planner](apps/planning/retirement_contribution/README.md) — Estimate annual retirement contributions including employer match.
- [Sleep Cycle Planner](apps/planning/sleep_cycle_planner/README.md) — Estimate sleep duration and cycle count between bedtime and wake time.
- [Study Scheduler](apps/planning/study_scheduler/README.md) — Allocate study time evenly across subjects and days.
- [Travel Budget](apps/planning/travel_budget/README.md) — Estimate total trip cost from daily and fixed expenses.
- [Weekly Goal Splitter](apps/planning/weekly_goal_splitter/README.md) — Break a measurable goal into weekday and weekend targets.
- [Workout Volume Planner](apps/planning/workout_volume/README.md) — Calculate resistance-training volume from sets, reps, and weight.

## Text Tools

- [Anagram Checker](apps/text_tools/anagram_checker/README.md) — Compare two phrases separated by a vertical bar for anagram equality.
- [Caesar Cipher](apps/text_tools/caesar_cipher/README.md) — Encode text with a classic three-letter Caesar shift.
- [Duplicate Line Remover](apps/text_tools/duplicate_line_remover/README.md) — Remove repeated lines while preserving first-seen order.
- [Email Masker](apps/text_tools/email_masker/README.md) — Mask email usernames while preserving domains.
- [Initials Maker](apps/text_tools/initials_maker/README.md) — Create initials from a person's or organization's name.
- [Line Sorter](apps/text_tools/line_sorter/README.md) — Sort nonempty text lines case-insensitively.
- [Markdown Link Extractor](apps/text_tools/markdown_link_extractor/README.md) — Extract labels and targets from inline Markdown links.
- [Morse Code Encoder](apps/text_tools/morse_encoder/README.md) — Encode letters and digits as International Morse code symbols.
- [Palindrome Checker](apps/text_tools/palindrome_checker/README.md) — Check whether text reads the same after normalization.
- [Password Strength Coach](apps/text_tools/password_strength/README.md) — Score password variety and length without storing the input.
- [Pig Latin Translator](apps/text_tools/pig_latin/README.md) — Translate simple English words into playful Pig Latin.
- [Reading Time Estimator](apps/text_tools/reading_time/README.md) — Estimate reading and speaking time from word count.
- [ROT13 Encoder](apps/text_tools/rot13_encoder/README.md) — Apply the reversible ROT13 substitution to text.
- [Sentence Statistics](apps/text_tools/sentence_stats/README.md) — Summarize sentence count and average sentence length.
- [Slugifier](apps/text_tools/slugifier/README.md) — Turn a title into a lowercase URL-friendly slug.
- [Smart Title Case](apps/text_tools/smart_title_case/README.md) — Capitalize a heading while keeping short connector words lowercase.
- [Vowel Histogram](apps/text_tools/vowel_histogram/README.md) — Count each vowel and draw a small text histogram.
- [Whitespace Cleaner](apps/text_tools/whitespace_cleaner/README.md) — Collapse repeated horizontal whitespace and trim every line.
- [Word Counter](apps/text_tools/word_counter/README.md) — Count lines, words, and characters in text.
- [Word Frequency Counter](apps/text_tools/word_frequency/README.md) — List words by descending frequency.

## Safety and accessibility

Apps avoid network calls, destructive filesystem changes, animation, color-only status, and mouse-only input. Terminal output stays readable at narrow widths; interactive apps accept keyboard input and also offer noninteractive demos.

## License

MIT. See `LICENSE`.

## Support this project

If this project saves you time, you can
[buy me a coffee](https://www.paypal.com/donate/?hosted_button_id=Q9VC7B42R7K82)
via PayPal. Thank you!
