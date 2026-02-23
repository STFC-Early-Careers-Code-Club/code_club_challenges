# Rust Code Challenge: Weather Station Monitor


## Your Task

Complete the skeleton code in `src/main.rs`:

1. **Define the WeatherAlert enum** - Add variants that carry data (algebraic data types)
2. **Implement input validation** - Use `Result<T, E>` instead of exceptions to validate sensor readings
3. **Detect weather alerts** - Return the correct enum variant based on weather conditions
4. **Describe alerts with pattern matching** - Use `match` to destructure and handle each enum variant
5. **Implement the Summary trait** - Define shared behaviour through traits, not inheritance
6. **Look up stations** - Use `Option<T>` instead of null for safe lookups
7. **Filter readings with iterators** - Use zero-cost iterator chains with closures

## Running the Code

```bash
# From the 12/ directory
cargo run
```

The code compiles and runs from the start! As you complete each TODO, the output will change from placeholder values to correct results.

## Expected Output (completed solution)

```
=== Weather Station Network Monitor ===

--- Adding Readings to Manchester ---
  Added: 12.5°C, 25.0 km/h, 70.0%
  Added: 38.0°C, 15.0 km/h, 45.0%
  Added: 3.0°C, 90.0 km/h, 85.0%
  Added: 22.0°C, 65.0 km/h, 55.0%
  Added: -5.0°C, 30.0 km/h, 80.0%

--- Testing Invalid Readings ---
  Rejected: Invalid temperature: 100°C (must be between -100 and 60)
  Rejected: Invalid wind speed: -5 km/h (must be >= 0)
  Rejected: Invalid humidity: 150% (must be between 0 and 100)

--- Station Summaries ---
  Station 'Manchester': 5 readings, avg temp: 14.1°C, max wind: 90.0 km/h
  Station 'London': 2 readings, avg temp: 32.2°C, max wind: 20.0 km/h

--- Station Lookup ---
  Found: Manchester (5 readings)
  'Edinburgh' not found

--- Weather Alerts ---
  Manchester:
    12.5°C, 25.0 km/h -> All clear - no alerts
    38.0°C, 15.0 km/h -> HIGH TEMP WARNING: 38.0°C
    3.0°C, 90.0 km/h -> STORM ALERT: wind 90.0 km/h, rain 42.5mm
    22.0°C, 65.0 km/h -> HIGH WIND WARNING: 65.0 km/h
    -5.0°C, 30.0 km/h -> All clear - no alerts
  London:
    28.0°C, 10.0 km/h -> All clear - no alerts
    36.5°C, 20.0 km/h -> HIGH TEMP WARNING: 36.5°C

--- Hot Reading Analysis ---
  Manchester has 1 reading(s) above 30.0°C
    38.0°C, 15.0 km/h
  London has 1 reading(s) above 30.0°C
    36.5°C, 20.0 km/h

=== Monitor Complete ===
```

## Hints

- Enum variants with data: `VariantName(Type)` or `VariantName { field: Type }`
- `match` must be exhaustive - handle every variant (or use `_ =>` as a catch-all)
- `Result<T, E>` is either `Ok(value)` or `Err(error)`
- `Option<T>` is either `Some(value)` or `None`
- Trait syntax: `trait Name { fn method(&self) -> Type; }`
- Iterator chain: `.iter().filter(|x| condition).collect()`
- `&self` = immutable borrow, `&mut self` = mutable borrow
- `format!()` returns a `String`, `println!()` prints to console
- The `'a` in function signatures is a "lifetime" - it tells the compiler how long references are valid

## Bonus Challenges

1. Add a `Fog(f64)` variant to `WeatherAlert` for visibility in km, and handle it in all match arms
2. Implement `std::fmt::Display` for `WeatherAlert` so you can use `println!("{}", alert)` instead of `describe_alert()`
3. Add a `worst_alert(&self) -> WeatherAlert` method to `Station` that returns the most severe alert across all readings
4. Write a `network_report()` function that uses iterator chains across all stations to find the highest temperature, the windiest station, and the total number of readings

Good luck!
