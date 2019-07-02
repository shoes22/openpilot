from cereal import car, log

# Priority
class Priority:
  LOWEST = 0
  LOW_LOWEST = 1
  LOW = 2
  MID = 3
  HIGH = 4
  HIGHEST = 5

AlertSize = log.ControlsState.AlertSize
AlertStatus = log.ControlsState.AlertStatus
AudibleAlert = car.CarControl.HUDControl.AudibleAlert
VisualAlert = car.CarControl.HUDControl.VisualAlert

class Alert(object):
  def __init__(self,
               alert_type,
               alert_text_1,
               alert_text_2,
               alert_status,
               alert_size,
               alert_priority,
               visual_alert,
               audible_alert,
               duration_sound,
               duration_hud_alert,
               duration_text,
               alert_rate=0.):

    self.alert_type = alert_type
    self.alert_text_1 = alert_text_1
    self.alert_text_2 = alert_text_2
    self.alert_status = alert_status
    self.alert_size = alert_size
    self.alert_priority = alert_priority
    self.visual_alert = visual_alert
    self.audible_alert = audible_alert

    self.duration_sound = duration_sound
    self.duration_hud_alert = duration_hud_alert
    self.duration_text = duration_text

    self.start_time = 0.
    self.alert_rate = alert_rate

    # typecheck that enums are valid on startup
    tst = car.CarControl.new_message()
    tst.hudControl.visualAlert = self.visual_alert

  def __str__(self):
    return self.alert_text_1 + "/" + self.alert_text_2 + " " + str(self.alert_priority) + "  " + str(
      self.visual_alert) + " " + str(self.audible_alert)

  def __gt__(self, alert2):
    return self.alert_priority > alert2.alert_priority


ALERTS = [
  # Miscellaneous alerts
  Alert(
      "enable",
      "",
      "",
      AlertStatus.normal, AlertSize.none,
      Priority.MID, VisualAlert.none, AudibleAlert.chimeEngage, .2, 0., 0.),

  Alert(
      "disable",
      "",
      "",
      AlertStatus.normal, AlertSize.none,
      Priority.MID, VisualAlert.none, AudibleAlert.chimeDisengage, .2, 0., 0.),

  Alert(
      "fcw",
      "BRAKE!",
      "Risk of Collision",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.fcw, AudibleAlert.chimeWarningRepeat, 1., 2., 2.),

  Alert(
      "steerSaturated",
      "TAKE CONTROL",
      "Turn Exceeds Hardcoded Steering Limit",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.chimePrompt, 1., 2., 3.),

  Alert(
      "steerTempUnavailable",
      "TAKE CONTROL",
      "Steering Temporarily Unavailable",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.chimeWarning1, .4, 2., 3.),

  Alert(
      "steerTempUnavailableMute",
      "TAKE CONTROL",
      "Steering Temporarily Unavailable",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, .2, .2, .2),

  Alert(
      "preDriverDistracted",
      "KEEP EYES ON ROAD: Alex Appears Distracted",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.none, .0, .1, .1, alert_rate=0.75),

  Alert(
      "promptDriverDistracted",
      "KEEP EYES ON ROAD",
      "Alex Appears Distracted",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, .1, .1),

  Alert(
      "driverDistracted",
      "DISENGAGE IMMEDIATELY",
      "Alex Was Distracted",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGH, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, .1, .1),

  Alert(
      "preDriverUnresponsive",
      "TOUCH STEERING WHEEL: No Driver Monitoring",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW, VisualAlert.steerRequired, AudibleAlert.none, .0, .1, .1, alert_rate=0.75),

  Alert(
      "promptDriverUnresponsive",
      "TOUCH STEERING WHEEL",
      "Alex Is Unresponsive",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, .1, .1),

  Alert(
      "driverUnresponsive",
      "DISENGAGE IMMEDIATELY",
      "Alex Was Unresponsive",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGH, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, .1, .1),

  Alert(
      "driverMonitorOff",
      "DRIVER MONITOR IS UNAVAILABLE",
      "Accuracy Is Low",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, .4, 0., 4.),

  Alert(
      "driverMonitorOn",
      "DRIVER MONITOR IS AVAILABLE",
      "Accuracy Is High",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, .4, 0., 4.),

  Alert(
      "geofence",
      "DISENGAGEMENT REQUIRED",
      "Not in Geofenced Area",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.HIGH, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, .1, .1, .1),

  Alert(
      "startup",
      "Welcome to Alex\'s car!",
      "Make sure your seatbelts are fastened.",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., 15.),

  Alert(
      "startupNoControl",
      "Dashcam mode",
      "Always keep hands on wheel and eyes on road",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., 15.),

  Alert(
      "startupNoCar",
      "Dashcam mode with unsupported car",
      "Always keep hands on wheel and eyes on road",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., 15.),

  Alert(
      "ethicalDilemma",
      "TAKE CONTROL IMMEDIATELY",
      "Ethical Dilemma Detected",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 3.),

  Alert(
      "steerTempUnavailableNoEntry",
      "alexpilot Unavailable",
      "Steering Temporarily Unavailable",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 0., 3.),

  Alert(
      "manualRestart",
      "TAKE CONTROL",
      "Resume Driving Manually",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "resumeRequired",
      "STOPPED",
      "Press Resume to Move",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "belowSteerSpeed",
      "TAKE CONTROL",
      "Steer Unavailable Below ",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning1, 0., 0., .1),

  Alert(
      "debugAlert",
      "DEBUG ALERT",
      "",
      AlertStatus.userPrompt, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.none, .1, .1, .1),

  # Non-entry only alerts
  Alert(
      "wrongCarModeNoEntry",
      "alexpilot Unavailable",
      "Main Switch Off",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 0., 3.),

  Alert(
      "dataNeededNoEntry",
      "alexpilot Unavailable",
      "Data Needed for Calibration. Upload Drive, Try Again",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 0., 3.),

  Alert(
      "outOfSpaceNoEntry",
      "alexpilot Unavailable",
      "Out of Storage Space",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 0., 3.),

  Alert(
      "pedalPressedNoEntry",
      "alexpilot Unavailable",
      "Pedal Pressed During Attempt",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, "brakePressed", AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "speedTooLowNoEntry",
      "alexpilot Unavailable",
      "Speed Too Low",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "brakeHoldNoEntry",
      "alexpilot Unavailable",
      "Brake Hold Active",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "parkBrakeNoEntry",
      "alexpilot Unavailable",
      "Park Brake Engaged",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "lowSpeedLockoutNoEntry",
      "alexpilot Unavailable",
      "Cruise Fault: Restart the Car",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "lowBatteryNoEntry",
      "alexpilot Unavailable",
      "Low Battery",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "sensorDataInvalidNoEntry",
      "alexpilot Unavailable",
      "No Data from EON Sensors",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  # Cancellation alerts causing soft disabling
  Alert(
      "overheat",
      "TAKE CONTROL IMMEDIATELY",
      "System Overheated",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "wrongGear",
      "TAKE CONTROL IMMEDIATELY",
      "Gear not D",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "calibrationInvalid",
      "TAKE CONTROL IMMEDIATELY",
      "Calibration Invalid: Reposition EON and Recalibrate",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "calibrationIncomplete",
      "TAKE CONTROL IMMEDIATELY",
      "Calibration in Progress",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "doorOpen",
      "TAKE CONTROL IMMEDIATELY",
      "Door Open",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "seatbeltNotLatched",
      "TAKE CONTROL IMMEDIATELY",
      "Seatbelt Unlatched",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "espDisabled",
      "TAKE CONTROL IMMEDIATELY",
      "ESP Off",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "lowBattery",
      "TAKE CONTROL IMMEDIATELY",
      "Low Battery",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "commIssue",
      "TAKE CONTROL IMMEDIATELY",
      "Communication Issue between Processes",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "radarCanError",
      "TAKE CONTROL IMMEDIATELY",
      "Radar Error: Restart the Car",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  Alert(
      "radarFault",
      "TAKE CONTROL IMMEDIATELY",
      "Radar Error: Restart the Car",
      AlertStatus.critical, AlertSize.full,
      Priority.MID, VisualAlert.steerRequired, AudibleAlert.chimeWarning2, .1, 2., 2.),

  # Cancellation alerts causing immediate disabling
  Alert(
      "controlsFailed",
      "TAKE CONTROL IMMEDIATELY",
      "Controls Failed",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "controlsMismatch",
      "TAKE CONTROL IMMEDIATELY",
      "Controls Mismatch",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "canError",
      "TAKE CONTROL IMMEDIATELY",
      "CAN Error: Check Connections",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "steerUnavailable",
      "TAKE CONTROL IMMEDIATELY",
      "LKAS Fault: Restart the Car",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "brakeUnavailable",
      "TAKE CONTROL IMMEDIATELY",
      "Cruise Fault: Restart the Car",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "gasUnavailable",
      "TAKE CONTROL IMMEDIATELY",
      "Gas Fault: Restart the Car",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "reverseGear",
      "TAKE CONTROL IMMEDIATELY",
      "Reverse Gear",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "cruiseDisabled",
      "TAKE CONTROL IMMEDIATELY",
      "Cruise Is Off",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  Alert(
      "plannerError",
      "TAKE CONTROL IMMEDIATELY",
      "Planner Solution Error",
      AlertStatus.critical, AlertSize.full,
      Priority.HIGHEST, VisualAlert.steerRequired, AudibleAlert.chimeWarningRepeat, 1., 3., 4.),

  # not loud cancellations (user is in control)
  Alert(
      "noTarget",
      "alexpilot Canceled",
      "No close lead car",
      AlertStatus.normal, AlertSize.mid,
      Priority.HIGH, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  Alert(
      "speedTooLow",
      "alexpilot Canceled",
      "Speed too low",
      AlertStatus.normal, AlertSize.mid,
      Priority.HIGH, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  Alert(
      "invalidGiraffeHonda",
      "Invalid Giraffe Configuration",
      "Set 0111 for alexpilot. 1011 for stock",
      AlertStatus.normal, AlertSize.mid,
      Priority.HIGH, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  # Cancellation alerts causing non-entry
  Alert(
      "overheatNoEntry",
      "alexpilot Unavailable",
      "System overheated",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "wrongGearNoEntry",
      "alexpilot Unavailable",
      "Gear not D",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "calibrationInvalidNoEntry",
      "alexpilot Unavailable",
      "Calibration Invalid: Reposition EON and Recalibrate",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "calibrationIncompleteNoEntry",
      "alexpilot Unavailable",
      "Calibration in Progress",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "doorOpenNoEntry",
      "alexpilot Unavailable",
      "Door open",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "seatbeltNotLatchedNoEntry",
      "alexpilot Unavailable",
      "Seatbelt unlatched",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "espDisabledNoEntry",
      "alexpilot Unavailable",
      "ESP Off",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "geofenceNoEntry",
      "alexpilot Unavailable",
      "Not in Geofenced Area",
      AlertStatus.normal, AlertSize.mid,
      Priority.MID, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "radarCanErrorNoEntry",
      "alexpilot Unavailable",
      "Radar Error: Restart the Car",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "radarFaultNoEntry",
      "alexpilot Unavailable",
      "Radar Error: Restart the Car",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "controlsFailedNoEntry",
      "alexpilot Unavailable",
      "Controls Failed",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "canErrorNoEntry",
      "alexpilot Unavailable",
      "CAN Error: Check Connections",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "steerUnavailableNoEntry",
      "alexpilot Unavailable",
      "LKAS Fault: Restart the Car",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "brakeUnavailableNoEntry",
      "alexpilot Unavailable",
      "Cruise Fault: Restart the Car",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "gasUnavailableNoEntry",
      "alexpilot Unavailable",
      "Gas Error: Restart the Car",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "reverseGearNoEntry",
      "alexpilot Unavailable",
      "Reverse Gear",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "cruiseDisabledNoEntry",
      "alexpilot Unavailable",
      "Cruise is Off",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "noTargetNoEntry",
      "alexpilot Unavailable",
      "No Close Lead Car",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "plannerErrorNoEntry",
      "alexpilot Unavailable",
      "Planner Solution Error",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeError, .4, 2., 3.),

  Alert(
      "invalidGiraffeHondaNoEntry",
      "alexpilot Unavailable",
      "Set 0111 for alexpilot. 1011 for stock",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  Alert(
      "commIssueNoEntry",
      "alexpilot unavailable",
      "Communication Issue between Processes",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW, VisualAlert.none, AudibleAlert.chimeDisengage, .4, 2., 3.),

  # permanent alerts
  Alert(
      "steerUnavailablePermanent",
      "LKAS Fault: Restart the car to engage",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "brakeUnavailablePermanent",
      "Cruise Fault: Restart the car to engage",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "lowSpeedLockoutPermanent",
      "Cruise Fault: Restart the car to engage",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "calibrationIncompletePermanent",
      "Calibration in Progress: ",
      "Drive Above ",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "invalidGiraffeHondaPermanent",
      "Invalid Giraffe Configuration",
      "Set 0111 for alexpilot. 1011 for stock",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "sensorDataInvalidPermanent",
      "No Data from EON Sensors",
      "Reboot your EON",
      AlertStatus.normal, AlertSize.mid,
      Priority.LOW_LOWEST, VisualAlert.none, AudibleAlert.none, 0., 0., .2),

  Alert(
      "vehicleModelInvalid",
      "Vehicle Parameter Identification Failed",
      "",
      AlertStatus.normal, AlertSize.small,
      Priority.LOWEST, VisualAlert.steerRequired, AudibleAlert.none, .0, .0, .1),
]
