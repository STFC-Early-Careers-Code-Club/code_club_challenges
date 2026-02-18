// Weather Station Network Monitor
// ================================
//
// Complete the TODOs below to build a weather monitoring system
// that demonstrates key Rust concepts from the lecture.
//
// Run with: cargo run

// ============================================================
// DATA TYPES (provided for you)
// ============================================================

/// A single weather reading from a station sensor.
#[derive(Debug)]
struct Reading {
    temperature: f64, // in °C
    wind_speed: f64,  // in km/h
    humidity: f64,    // percentage (0-100)
}

/// A weather station that collects readings.
#[derive(Debug)]
struct Station {
    name: String,
    readings: Vec<Reading>,
}

// ============================================================
// TODO 1: Complete the WeatherAlert enum
//
// In Java, enums are just simple values. In Rust, each enum
// variant can CARRY DATA - this is called an algebraic data
// type (ADT). It makes "invalid states unrepresentable."
//
// Add three more variants:
//   - HighTemperature(f64)    -- carries the temperature value
//   - HighWind(f64)           -- carries the wind speed value
//   - Storm { wind_speed: f64, rainfall_mm: f64 }
//                             -- a "struct variant" with named fields
// ============================================================

#[derive(Debug)]
enum WeatherAlert {
    Clear,
    // Add your variants here
}

// ============================================================
// Reading methods
// ============================================================

impl Reading {
    // ========================================================
    // TODO 2: Implement input validation using Result<T, E>
    //
    // Rust has NO exceptions! Instead, functions return
    // Result<T, E> which is either Ok(value) or Err(error).
    // Errors are part of the return type, not a separate
    // control flow mechanism.
    //
    // Validate:
    //   - temperature must be between -100.0 and 60.0
    //   - wind_speed must be >= 0.0
    //   - humidity must be between 0.0 and 100.0
    //
    // Return Err(String) with a message if invalid,
    // or Ok(Reading { ... }) if all values are valid.
    // ========================================================
    fn validate(temperature: f64, wind_speed: f64, humidity: f64) -> Result<Reading, String> {
        // Replace this: add validation checks before creating the Reading.
        // Return Err("message".to_string()) for invalid values.
        Ok(Reading {
            temperature,
            wind_speed,
            humidity,
        })
    }

    // ========================================================
    // TODO 3: Implement weather alert detection
    //
    // Check conditions and return the appropriate WeatherAlert
    // variant. Each variant carries the relevant data with it!
    //
    //   - wind > 80 AND temp < 5  -> Storm (rainfall = humidity * 0.5)
    //   - temp > 35               -> HighTemperature
    //   - wind > 60               -> HighWind
    //   - otherwise               -> Clear
    //
    // Note: Requires TODO 1 to be completed first!
    // ========================================================
    fn check_alert(&self) -> WeatherAlert {
        // Replace with condition checks returning the right variant
        WeatherAlert::Clear
    }
}

// ============================================================
// TODO 4: Implement pattern matching for WeatherAlert
//
// Rust's `match` expression lets you destructure enum variants
// and extract the data they carry. Every variant MUST be
// handled (exhaustive matching) - the compiler enforces this!
//
// After TODO 1, the wildcard `_` below catches your new
// variants. Replace it with specific match arms:
//
//   WeatherAlert::HighTemperature(temp) =>
//       format!("HIGH TEMP WARNING: {temp:.1}°C")
//
//   WeatherAlert::HighWind(speed) =>
//       format!("HIGH WIND WARNING: {speed:.1} km/h")
//
//   WeatherAlert::Storm { wind_speed, rainfall_mm } =>
//       format!("STORM ALERT: wind {wind_speed:.1} km/h, rain {rainfall_mm:.1}mm")
// ============================================================

fn describe_alert(alert: &WeatherAlert) -> String {
    match alert {
        WeatherAlert::Clear => String::from("All clear - no alerts"),
        _ => String::from("Unknown alert"), // TODO 4: replace with specific arms
    }
}

// ============================================================
// TODO 5: Define and implement the Summary trait
//
// Java uses INHERITANCE for shared behaviour. Rust uses TRAITS
// instead - they define what methods a type must implement,
// without the problems of the diamond inheritance pattern.
//
// The trait is defined below with its method signature.
// Complete the `impl Summary for Station` block to return:
//   "Station '<name>': <n> readings, avg temp: <t>°C, max wind: <w> km/h"
//
// Hint: use self.average_temperature() and self.max_wind_speed()
//       which are already implemented below.
// ============================================================

trait Summary {
    fn summary(&self) -> String;
}

impl Summary for Station {
    fn summary(&self) -> String {
        // Replace this placeholder with a proper formatted summary
        format!("Station '{}': (summary not yet implemented)", self.name)
    }
}

// ============================================================
// Station methods (mostly provided)
// ============================================================

impl Station {
    /// Create a new station with the given name.
    fn new(name: &str) -> Station {
        Station {
            name: name.to_string(),
            readings: Vec::new(),
        }
    }

    /// Add a reading to the station.
    /// Note: &mut self - we need a MUTABLE reference to modify the station!
    /// In Rust, everything is immutable by default. You must opt in to mutation.
    fn add_reading(&mut self, reading: Reading) {
        self.readings.push(reading);
    }

    /// Calculate the average temperature across all readings.
    /// Note: &self - an IMMUTABLE reference, we're only reading data.
    fn average_temperature(&self) -> f64 {
        if self.readings.is_empty() {
            return 0.0;
        }
        let sum: f64 = self.readings.iter().map(|r| r.temperature).sum();
        sum / self.readings.len() as f64
    }

    /// Find the maximum wind speed across all readings.
    fn max_wind_speed(&self) -> f64 {
        self.readings
            .iter()
            .map(|r| r.wind_speed)
            .fold(0.0_f64, f64::max)
    }

    // ========================================================
    // TODO 7: Return readings above a temperature threshold
    //
    // Use Rust's zero-cost iterator chain:
    //   self.readings.iter()
    //       .filter(|r| ...)   // closure! like Java lambdas
    //       .collect()         // collect into a Vec
    //
    // Unlike Java streams which create iterator objects at
    // runtime, Rust compiles these chains into optimised loops
    // with NO allocation overhead. Readable AND fast!
    //
    // The return type Vec<&Reading> means "a vector of
    // references to readings" - we borrow, not copy.
    // ========================================================
    fn hot_readings(&self, threshold: f64) -> Vec<&Reading> {
        // Replace with an iterator chain
        Vec::new()
    }
}

// ============================================================
// TODO 6: Implement station lookup returning Option<T>
//
// Java has null. Rust has NO null! Instead, it uses Option<T>
// which is either Some(value) or None. This makes the absence
// of a value EXPLICIT in the type system - no more
// NullPointerException at runtime!
//
// Search through the stations slice and return:
//   Some(station_reference) if found, or None if not found.
//
// Hint: you can use stations.iter().find(|s| ...)
//
// The 'a is a "lifetime" - it tells Rust the returned
// reference is valid as long as the stations slice is.
// Don't worry too much about it, just keep it in the signature.
// ============================================================

fn find_station<'a>(stations: &'a [Station], name: &str) -> Option<&'a Station> {
    // Replace with a search through stations
    None
}

// ============================================================
// MAIN - do not modify (tests all your TODOs!)
// ============================================================

fn main() {
    println!("=== Weather Station Network Monitor ===\n");

    // --- Create stations (note: `mut` because we'll add readings) ---
    let mut manchester = Station::new("Manchester");
    let mut london = Station::new("London");

    // --- Add readings with validation (tests TODO 2) ---
    println!("--- Adding Readings to Manchester ---");
    let test_data = vec![
        (12.5, 25.0, 70.0),
        (38.0, 15.0, 45.0),  // hot!
        (3.0, 90.0, 85.0),   // stormy!
        (22.0, 65.0, 55.0),  // windy
        (-5.0, 30.0, 80.0),
    ];

    for (temp, wind, humidity) in &test_data {
        match Reading::validate(*temp, *wind, *humidity) {
            Ok(reading) => {
                println!(
                    "  Added: {:.1}°C, {:.1} km/h, {:.1}%",
                    reading.temperature, reading.wind_speed, reading.humidity
                );
                manchester.add_reading(reading);
            }
            Err(e) => println!("  Rejected: {}", e),
        }
    }

    // --- Test invalid readings (tests TODO 2) ---
    println!("\n--- Testing Invalid Readings ---");
    let invalid_data = vec![
        (100.0, 10.0, 50.0), // temp too high
        (20.0, -5.0, 50.0),  // negative wind speed
        (20.0, 10.0, 150.0), // humidity over 100%
    ];

    for (temp, wind, humidity) in &invalid_data {
        match Reading::validate(*temp, *wind, *humidity) {
            Ok(_) => println!(
                "  ({:.1}, {:.1}, {:.1}) -> Accepted (should be rejected after TODO 2!)",
                temp, wind, humidity
            ),
            Err(e) => println!("  Rejected: {}", e),
        }
    }

    // --- Add London readings ---
    if let Ok(r) = Reading::validate(28.0, 10.0, 50.0) {
        london.add_reading(r);
    }
    if let Ok(r) = Reading::validate(36.5, 20.0, 40.0) {
        london.add_reading(r);
    }

    // --- Station summaries (tests TODO 5) ---
    let stations = vec![manchester, london];
    println!("\n--- Station Summaries ---");
    for station in &stations {
        println!("  {}", station.summary());
    }

    // --- Station lookup (tests TODO 6) ---
    println!("\n--- Station Lookup ---");
    match find_station(&stations, "Manchester") {
        Some(s) => println!("  Found: {} ({} readings)", s.name, s.readings.len()),
        None => println!("  'Manchester' not found (implement TODO 6!)"),
    }
    match find_station(&stations, "Edinburgh") {
        Some(s) => println!("  Found: {}", s.name),
        None => println!("  'Edinburgh' not found"),
    }

    // --- Weather alerts (tests TODOs 1, 3, 4) ---
    println!("\n--- Weather Alerts ---");
    for station in &stations {
        println!("  {}:", station.name);
        for reading in &station.readings {
            let alert = reading.check_alert();
            println!(
                "    {:.1}°C, {:.1} km/h -> {}",
                reading.temperature,
                reading.wind_speed,
                describe_alert(&alert)
            );
        }
    }

    // --- Hot readings analysis (tests TODO 7) ---
    println!("\n--- Hot Reading Analysis ---");
    for station in &stations {
        let hot = station.hot_readings(30.0);
        println!(
            "  {} has {} reading(s) above 30.0°C",
            station.name,
            hot.len()
        );
        for r in &hot {
            println!("    {:.1}°C, {:.1} km/h", r.temperature, r.wind_speed);
        }
    }

    println!("\n=== Monitor Complete ===");
}
