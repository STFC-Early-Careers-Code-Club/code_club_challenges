// Weather Station Network Monitor
// ================================
//
// SOLUTION - Complete implementation of all TODOs.
//
// Run with: cargo run

// ============================================================
// DATA TYPES
// ============================================================

#[derive(Debug)]
struct Reading {
    temperature: f64,
    wind_speed: f64,
    humidity: f64,
}

#[derive(Debug)]
struct Station {
    name: String,
    readings: Vec<Reading>,
}

// ============================================================
// TODO 1: WeatherAlert enum (COMPLETED)
//
// Each variant carries different data - this is an algebraic
// data type (ADT), something Java enums can't do!
// ============================================================

#[derive(Debug)]
enum WeatherAlert {
    Clear,
    HighTemperature(f64),
    HighWind(f64),
    Storm { wind_speed: f64, rainfall_mm: f64 },
}

// ============================================================
// Reading methods
// ============================================================

impl Reading {
    // ========================================================
    // TODO 2: Input validation with Result<T, E> (COMPLETED)
    // ========================================================
    fn validate(temperature: f64, wind_speed: f64, humidity: f64) -> Result<Reading, String> {
        if temperature < -100.0 || temperature > 60.0 {
            return Err(format!(
                "Invalid temperature: {}°C (must be between -100 and 60)",
                temperature
            ));
        }
        if wind_speed < 0.0 {
            return Err(format!(
                "Invalid wind speed: {} km/h (must be >= 0)",
                wind_speed
            ));
        }
        if humidity < 0.0 || humidity > 100.0 {
            return Err(format!(
                "Invalid humidity: {}% (must be between 0 and 100)",
                humidity
            ));
        }
        Ok(Reading {
            temperature,
            wind_speed,
            humidity,
        })
    }

    // ========================================================
    // TODO 3: Weather alert detection (COMPLETED)
    // ========================================================
    fn check_alert(&self) -> WeatherAlert {
        if self.wind_speed > 80.0 && self.temperature < 5.0 {
            WeatherAlert::Storm {
                wind_speed: self.wind_speed,
                rainfall_mm: self.humidity * 0.5,
            }
        } else if self.temperature > 35.0 {
            WeatherAlert::HighTemperature(self.temperature)
        } else if self.wind_speed > 60.0 {
            WeatherAlert::HighWind(self.wind_speed)
        } else {
            WeatherAlert::Clear
        }
    }
}

// ============================================================
// TODO 4: Pattern matching (COMPLETED)
// ============================================================

fn describe_alert(alert: &WeatherAlert) -> String {
    match alert {
        WeatherAlert::Clear => String::from("All clear - no alerts"),
        WeatherAlert::HighTemperature(temp) => {
            format!("HIGH TEMP WARNING: {temp:.1}°C")
        }
        WeatherAlert::HighWind(speed) => {
            format!("HIGH WIND WARNING: {speed:.1} km/h")
        }
        WeatherAlert::Storm {
            wind_speed,
            rainfall_mm,
        } => {
            format!("STORM ALERT: wind {wind_speed:.1} km/h, rain {rainfall_mm:.1}mm")
        }
    }
}

// ============================================================
// TODO 5: Summary trait (COMPLETED)
// ============================================================

trait Summary {
    fn summary(&self) -> String;
}

impl Summary for Station {
    fn summary(&self) -> String {
        format!(
            "Station '{}': {} readings, avg temp: {:.1}°C, max wind: {:.1} km/h",
            self.name,
            self.readings.len(),
            self.average_temperature(),
            self.max_wind_speed()
        )
    }
}

// ============================================================
// Station methods
// ============================================================

impl Station {
    fn new(name: &str) -> Station {
        Station {
            name: name.to_string(),
            readings: Vec::new(),
        }
    }

    fn add_reading(&mut self, reading: Reading) {
        self.readings.push(reading);
    }

    fn average_temperature(&self) -> f64 {
        if self.readings.is_empty() {
            return 0.0;
        }
        let sum: f64 = self.readings.iter().map(|r| r.temperature).sum();
        sum / self.readings.len() as f64
    }

    fn max_wind_speed(&self) -> f64 {
        self.readings
            .iter()
            .map(|r| r.wind_speed)
            .fold(0.0_f64, f64::max)
    }

    // ========================================================
    // TODO 7: Iterator-based filtering (COMPLETED)
    // ========================================================
    fn hot_readings(&self, threshold: f64) -> Vec<&Reading> {
        self.readings
            .iter()
            .filter(|r| r.temperature > threshold)
            .collect()
    }
}

// ============================================================
// TODO 6: Station lookup with Option<T> (COMPLETED)
// ============================================================

fn find_station<'a>(stations: &'a [Station], name: &str) -> Option<&'a Station> {
    stations.iter().find(|s| s.name == name)
}

// ============================================================
// MAIN
// ============================================================

fn main() {
    println!("=== Weather Station Network Monitor ===\n");

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
