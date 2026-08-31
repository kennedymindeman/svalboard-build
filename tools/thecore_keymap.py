#!/usr/bin/env python3
"""Build thecore/keymap.html: TheCore's key map, toggled by race and co-op commander.

Usage: python3 tools/thecore_keymap.py

Reads the two .SC2Hotkeys files in thecore/, classifies every [Commands] entry
that names a unit into the melee races and the co-op commanders that field it,
and writes a self-contained page (inline CSS/JS, embedded JSON, no network) at
thecore/keymap.html.  Unclassifiable units land in an "Unclassified" bucket
whose count and names are printed to stderr.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from thecore_keys import FINGERS, MODS  # noqa: E402

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = [
    ("TheCore 5.0 Right Plus", "thecore/TheCore_5.0_Right_Plus.SC2Hotkeys"),
    ("TheCore 6.0 Right", "thecore/TheCore6g_right_US_qwerty.SC2Hotkeys"),
]
OUT = "thecore/keymap.html"

MELEE = ["Terran", "Zerg", "Protoss"]
# Co-op commanders present in these files, with the melee race whose units they
# also field.  Mengsk has no units in either file, so he is not listed.
COMMANDERS = {
    "Raynor": "Terran",
    "Kerrigan": "Zerg",
    "Artanis": "Protoss",
    "Swann": "Terran",
    "Zagara": "Zerg",
    "Vorazun": "Protoss",
    "Karax": "Protoss",
    "Abathur": "Zerg",
    "Alarak": "Protoss",
    "Nova": "Terran",
    "Stukov": "Terran",
    "Fenix": "Protoss",
    "Dehaka": "Zerg",
    "Han & Horner": "Terran",
    "Tychus": "Terran",
    "Zeratul": "Protoss",
    "Stetmann": "Zerg",
}
GLOBAL = "Global"
UNCLASSIFIED = "Unclassified"
FACTIONS = MELEE + list(COMMANDERS) + [GLOBAL, UNCLASSIFIED]

# Exact unit name -> the factions that own it.  A melee race here means "plain
# melee unit": it shows for that race and for every commander of that race.  A
# commander list means the unit is commander-specific.  Campaign-era units with
# no single co-op owner (Reaver, Harvester, MothershipCore, ...) are filed under
# their race so they appear in every view of that race rather than disappearing.
UNIT_FACTIONS = {
    'Adept': ['Protoss'],
    'AlarakCoop': ['Alarak'],
    'AlarakReviveBeacon': ['Alarak'],
    'ArbiterMP': ['Protoss'],
    'Archon': ['Protoss'],
    'Armory': ['Terran'],
    'Baneling': ['Zerg'],
    'BanelingBurrowed': ['Zerg'],
    'BanelingNest': ['Zerg'],
    'BanelingNestStetmann': ['Stetmann'],
    'BanelingStetmann': ['Stetmann'],
    'BanelingStetmannBurrowed': ['Stetmann'],
    'Banshee': ['Terran'],
    'Banshee_BlackOps': ['Nova'],
    'Barracks': ['Terran'],
    'BarracksFlying': ['Terran'],
    'BarracksTechLab': ['Terran'],
    'BarracksTechReactor': ['Terran'],
    'Battlecruiser': ['Terran'],
    'BileLauncherZagara': ['Zagara'],
    'BroodLordStetmann': ['Stetmann'],
    'Brutalisk': ['Abathur'],
    'Bunker': ['Terran'],
    'Carrier': ['Protoss'],
    'CommandCenter': ['Terran'],
    'Corruptor': ['Zerg'],
    'CorruptorStetmann': ['Stetmann'],
    'CorsairMP': ['Vorazun'],
    'CreepTumorBurrowed': ['Zerg'],
    'CyberneticsCore': ['Protoss'],
    'CybrosEscortDownloader': ['Protoss'],
    'Cyclone': ['Terran'],
    'DarkArchon': ['Vorazun'],
    'DarkPylon': ['Vorazun'],
    'DarkShrine': ['Protoss'],
    'DarkTemplar': ['Protoss'],
    'DarkTemplarShakuras': ['Vorazun'],
    'DarkTemplarTaldarim': ['Protoss'],
    'DehakaBarracks': ['Dehaka'],
    'DehakaBarracksUprooted': ['Dehaka'],
    'DehakaCoop': ['Dehaka'],
    'DehakaCoopReviveCocoon': ['Dehaka'],
    'DehakaDakrun': ['Dehaka'],
    'DehakaDakrunStructure': ['Dehaka'],
    'DehakaDrone': ['Dehaka'],
    'DehakaGlevig': ['Dehaka'],
    'DehakaGlevigStructure': ['Dehaka'],
    'DehakaGuardian': ['Dehaka'],
    'DehakaHatchery': ['Dehaka'],
    'DehakaHatcheryUprooted': ['Dehaka'],
    'DehakaHydraliskLevel2': ['Dehaka'],
    'DehakaMirrorImage': ['Dehaka'],
    'DehakaMurvar': ['Dehaka'],
    'DehakaMurvarStructure': ['Dehaka'],
    'DehakaNydusDestroyer': ['Dehaka'],
    'DehakaNydusDestroyerTimedNoFood': ['Dehaka'],
    'DehakaPrimalSwarmHost': ['Dehaka'],
    'DehakaPrimalSwarmHostBurrowed': ['Dehaka'],
    'DehakaRoachLevel2': ['Dehaka'],
    'DehakaSwarmHost': ['Dehaka'],
    'DehakaSwarmHostBurrowed': ['Dehaka'],
    'DehakaUltraliskLevel2': ['Dehaka'],
    'DehakaUltraliskLevel3': ['Dehaka'],
    'DehakaZerglingLevel2': ['Dehaka'],
    'DevilDog': ['Terran'],
    'Devourer': ['Abathur'],
    'Disruptor': ['Protoss'],
    'DrakkenLaserDrillCoop': ['Swann'],
    'Drone': ['Zerg'],
    'EngineeringBay': ['Terran'],
    'EvolutionChamber': ['Zerg'],
    'EvolutionChamberStetmann': ['Stetmann'],
    'Factory': ['Terran'],
    'FactoryFlying': ['Terran'],
    'FactoryTechLab': ['Terran'],
    'FactoryTechReactor': ['Terran'],
    'FenixAltarOfPsiStorms': ['Fenix'],
    'FenixArbiter': ['Fenix'],
    'FenixClolarionCarrier': ['Fenix'],
    'FenixCoop': ['Fenix'],
    'FenixDragoon': ['Fenix'],
    'FenixKaldalisZealot': ['Fenix'],
    'FenixMojoScout': ['Fenix'],
    'FenixTaldarinImmortal': ['Fenix'],
    'FenixTalisAdept': ['Fenix'],
    'FenixWarbringerColossus': ['Fenix'],
    'Firebat': ['Raynor'],
    'FleetBeacon': ['Protoss'],
    'Forge': ['Protoss'],
    'FusionCore': ['Terran'],
    'GaryStetmann': ['Stetmann'],
    'Gateway': ['Protoss'],
    'Ghost': ['Terran'],
    'GhostAcademy': ['Terran'],
    'GhostAcademyNova': ['Nova'],
    'Ghost_BlackOps': ['Nova'],
    'GreaterSpire': ['Zerg'],
    'GreaterSpireStetmann': ['Stetmann'],
    'GuardianMP': ['Abathur'],
    'HHBattlecruiser': ['Han & Horner'],
    'HHBomberPlatform': ['Han & Horner'],
    'HHHellion': ['Han & Horner'],
    'HHHellionTank': ['Han & Horner'],
    'HHMercCompound': ['Han & Horner'],
    'HHMercStarportUpgraded': ['Han & Horner'],
    'HHRaven': ['Han & Horner'],
    'HHReaper': ['Han & Horner'],
    'HHSCV': ['Han & Horner'],
    'HHStarport': ['Han & Horner'],
    'HHStarportFlying': ['Han & Horner'],
    'HHVikingAssault': ['Han & Horner'],
    'HHVikingFighter': ['Han & Horner'],
    'HHWidowMine': ['Han & Horner'],
    'HHWraith': ['Han & Horner'],
    'Harvester': ['Protoss'],
    'Hatchery': ['Zerg'],
    'HatcheryStetmann': ['Stetmann'],
    'HealingDrone': ['Terran'],
    'Hellion': ['Terran'],
    'HellionBlackOps': ['Nova'],
    'Hercules': ['Swann'],
    'HighTemplar': ['Protoss'],
    'HighTemplarTaldarim': ['Alarak'],
    'Hive': ['Zerg'],
    'HotSHunter': ['Zerg'],
    'HotSHunterBurrowed': ['Zerg'],
    'HotSLeviathan': ['Abathur'],
    'HotSNoxious': ['Zerg'],
    'HotSRaptor': ['Kerrigan'],
    'HotSSplitterlingBig': ['Zagara'],
    'HotSSplitterlingBigBurrowed': ['Zagara'],
    'HotSSwarmling': ['Zagara'],
    'HotSTorrasque': ['Kerrigan'],
    'HugeSwarmQueen': ['Zagara'],
    'Hydralisk': ['Zerg'],
    'HydraliskDen': ['Zerg'],
    'HydraliskDenStetmann': ['Stetmann'],
    'HydraliskImpaler': ['Dehaka'],
    'HydraliskLurker': ['Dehaka'],
    'HydraliskStetmann': ['Stetmann'],
    'HyperionKorhal': ['Raynor'],
    'HyperionVoidCoop': ['Raynor'],
    'Immortal': ['Protoss'],
    'ImmortalShakuras': ['Protoss'],
    'InfestationPit': ['Zerg'],
    'InfestationPitStetmann': ['Stetmann'],
    'Infestor': ['Zerg'],
    'InfestorBurrowed': ['Zerg'],
    'InfestorStetmann': ['Stetmann'],
    'InfestorStetmannBurrowed': ['Stetmann'],
    'K5Kerrigan': ['Kerrigan'],
    'K5KerriganBurrowed': ['Kerrigan'],
    'KelMorianGrenadeTurret': ['Swann'],
    'KelMorianMissileTurret': ['Swann'],
    'KerriganGhostLab': ['Kerrigan'],
    'Lair': ['Zerg'],
    'LairStetmann': ['Stetmann'],
    'LargeSwarmQueen': ['Zagara'],
    'Larva': ['Zerg'],
    'LarvaStetmann': ['Stetmann'],
    'Liberator': ['Terran'],
    'Liberator_BlackOps': ['Nova'],
    'LocustMPFlying': ['Zerg'],
    'LurkerBurrowed': ['Zerg'],
    'LurkerDen': ['Zerg'],
    'LurkerDenMP': ['Zerg'],
    'LurkerDenStetmann': ['Stetmann'],
    'LurkerMP': ['Zerg'],
    'LurkerMPBurrowed': ['Zerg'],
    'LurkerStetmann': ['Stetmann'],
    'LurkerStetmannBurrowed': ['Stetmann'],
    'Marauder_BlackOps': ['Nova'],
    'Marine_BlackOps': ['Nova'],
    'Medic': ['Raynor'],
    'Medivac': ['Terran'],
    'Medivac_BlackOps': ['Nova'],
    'MercMedic': ['Terran'],
    'MissileTurret': ['Terran'],
    'Monitor': ['Protoss'],
    'Mothership': ['Protoss'],
    'MothershipAiur06': ['Artanis'],
    'MothershipCore': ['Protoss'],
    'Mutalisk': ['Zerg'],
    'MutaliskBroodlord': ['Kerrigan'],
    'MutaliskViper': ['Abathur'],
    'MutatorWidowMine': ['Terran'],
    'Nexus': ['Protoss'],
    'Nova': ['Nova'],
    'NovaACLaserTurret': ['Nova'],
    'NovaBoombot': ['Nova'],
    'NovaCoop': ['Nova'],
    'NovaDefensiveMatrixDrone': ['Nova'],
    'NovaReviveBeacon': ['Nova'],
    'NydusNetwork': ['Zerg'],
    'Observer': ['Protoss'],
    'Odin': ['Terran'],
    'Oracle': ['Protoss'],
    'OrbitalCommand': ['Terran'],
    'Overlord': ['Zerg'],
    'OverlordTransport': ['Zerg'],
    'Overseer': ['Zerg'],
    'OverseerStetmann': ['Stetmann'],
    'PerditionTurret': ['Swann'],
    'PerditionTurretUnderground': ['Swann'],
    'Phoenix': ['Protoss'],
    'PhoenixPurifier': ['Karax'],
    'PlanetaryFortress': ['Terran'],
    'PowerTowerStetmann': ['Stetmann'],
    'PrimalTownHall': ['Dehaka'],
    'Probe': ['Protoss'],
    'Queen': ['Zerg'],
    'QueenBurrowed': ['Zerg'],
    'QueenCoop': ['Zerg'],
    'Ravager': ['Zerg'],
    'RavagerAbathur': ['Abathur'],
    'RavagerStetmann': ['Stetmann'],
    'Raven': ['Terran'],
    'RavenRepairDrone': ['Terran'],
    'Raven_BlackOps': ['Nova'],
    'Reaper': ['Terran'],
    'Reaver': ['Protoss'],
    'Roach': ['Zerg'],
    'RoachBurrowed': ['Zerg'],
    'RoachCorpser': ['Zerg'],
    'RoachVile': ['Abathur'],
    'RoachVileBurrowed': ['Abathur'],
    'RoachWarren': ['Zerg'],
    'RoboticsBay': ['Protoss'],
    'RoboticsFacility': ['Protoss'],
    'RoboticsFacilityWarp': ['Protoss'],
    'SCV': ['Terran'],
    'SIArmory': ['Stukov'],
    'SIBarracks': ['Stukov'],
    'SIBarracksFlying': ['Stukov'],
    'SIBarracksTechLab': ['Stukov'],
    'SICivilianStructure': ['Stukov'],
    'SICivilianStructureFlying': ['Stukov'],
    'SICommandCenter': ['Stukov'],
    'SICommandCenterFlying': ['Stukov'],
    'SIEngineeringBay': ['Stukov'],
    'SIFactory': ['Stukov'],
    'SIFactoryFlying': ['Stukov'],
    'SIFactoryTechLab': ['Stukov'],
    'SIInfestedBunker': ['Stukov'],
    'SIInfestedBunkerUprooted': ['Stukov'],
    'SIMissileTurret': ['Stukov'],
    'SIMissileTurretFlying': ['Stukov'],
    'SIOverlord': ['Stukov'],
    'SIQueen': ['Stukov'],
    'SISCV': ['Stukov'],
    'SIStarport': ['Stukov'],
    'SIStarportFlying': ['Stukov'],
    'SIStarportTechLab': ['Stukov'],
    'SIVolatileInfested': ['Stukov'],
    'SJHyperion': ['Raynor'],
    'SOAMothershipv4': ['Alarak'],
    'ScienceVessel': ['Swann'],
    'Scourge': ['Zagara'],
    'ScourgeNest': ['Zagara'],
    'Sentry': ['Protoss'],
    'SentryAiur': ['Protoss'],
    'SentryFenix': ['Fenix'],
    'SentryPurifier': ['Karax'],
    'ShieldBattery': ['Protoss'],
    'SiegeTank': ['Terran'],
    'SiegeTank_BlackOps': ['Nova'],
    'SolarForge': ['Karax'],
    'SpawningPool': ['Zerg'],
    'SpawningPoolStetmann': ['Stetmann'],
    'Spectre': ['Terran'],
    'SpineCrawler': ['Zerg'],
    'SpineCrawlerStetmann': ['Stetmann'],
    'SpineCrawlerUprooted': ['Zerg'],
    'SpineCrawlerUprootedStetmann': ['Stetmann'],
    'Spire': ['Zerg'],
    'SpireStetmann': ['Stetmann'],
    'SporeCrawler': ['Zerg'],
    'SporeCrawlerStetmann': ['Stetmann'],
    'SporeCrawlerUprooted': ['Zerg'],
    'SporeCrawlerUprootedStetmann': ['Stetmann'],
    'Stalker': ['Protoss'],
    'StalkerShakuras': ['Vorazun'],
    'Stargate': ['Protoss'],
    'StargateWarp': ['Protoss'],
    'Starport': ['Terran'],
    'StarportFlying': ['Terran'],
    'StarportTechLab': ['Terran'],
    'StarportTechReactor': ['Terran'],
    'Stetmann': ['Stetmann'],
    'StukovApocalisk': ['Stukov'],
    'StukovInfestedDiamondBack': ['Stukov'],
    'StukovInfestedSiegeTank': ['Stukov'],
    'SuperGaryStetmann': ['Stetmann'],
    'SuperWarpGate': ['Protoss'],
    'SupplyDepot': ['Terran'],
    'SupplyDepotLowered': ['Terran'],
    'SwarmHost': ['Zerg'],
    'SwarmHostBurrowed': ['Zerg'],
    'SwarmHostBurrowedMP': ['Zerg'],
    'SwarmHostMP': ['Zerg'],
    'SwarmHostRooted': ['Zerg'],
    'SwarmHostSplitABurrowed': ['Zerg'],
    'SwarmHostSplitARooted': ['Zerg'],
    'SwarmHostSplitB': ['Zerg'],
    'SwarmHostSplitBBurrowed': ['Zerg'],
    'SwarmHostSplitBRooted': ['Zerg'],
    'SwarmQueen': ['Zagara'],
    'Tempest': ['Protoss'],
    'TempestPurifier': ['Protoss'],
    'TemplarArchive': ['Protoss'],
    'Thor': ['Terran'],
    'ThorWreckageSwann': ['Swann'],
    'Tosh': ['Terran'],
    'ToxicNest': ['Abathur'],
    'TwilightCouncil': ['Protoss'],
    'TychusArmory': ['Tychus'],
    'TychusCommandCenter': ['Tychus'],
    'TychusEngineeringBay': ['Tychus'],
    'TychusGhost': ['Tychus'],
    'TychusGhostAcademy': ['Tychus'],
    'TychusMarauder': ['Tychus'],
    'TychusMedic': ['Tychus'],
    'TychusMedivacPlatform': ['Tychus'],
    'TychusMercCompound': ['Tychus'],
    'TychusOdin': ['Tychus'],
    'TychusReaper': ['Tychus'],
    'TychusResearchCenter': ['Tychus'],
    'TychusSCV': ['Tychus'],
    'TychusSCVAutoTurret': ['Tychus'],
    'TychusWarhound': ['Tychus'],
    'TychusWarhoundAutoTurret': ['Tychus'],
    'Ultralisk': ['Zerg'],
    'UltraliskCavern': ['Zerg'],
    'UltraliskCavernStetmann': ['Stetmann'],
    'UltraliskStetmann': ['Stetmann'],
    'VikingAssault': ['Terran'],
    'Viper': ['Zerg'],
    'VoidRay': ['Protoss'],
    'VoidRiftUnselectable': ['Zerg'],
    'VorazunShadowGuard': ['Vorazun'],
    'Vulture': ['Raynor'],
    'WarpGate': ['Protoss'],
    'WarpPrism': ['Protoss'],
    'WarpPrismTaldarim': ['Alarak'],
    'WidowMine': ['Terran'],
    'Wraith': ['Swann'],
    'YagdraEggSmall': ['Dehaka'],
    'ZagaraCorruptor': ['Zagara'],
    'ZagaraVoidCoop': ['Zagara'],
    'ZagaraVoidCoopBurrowed': ['Zagara'],
    'Zealot': ['Protoss'],
    'ZealotAiur': ['Artanis'],
    'ZealotPurifier': ['Karax'],
    'ZealotShakuras': ['Vorazun'],
    'ZeratulCoop': ['Zeratul'],
    'ZeratulDarkArchon': ['Zeratul'],
    'ZeratulDarkTemplar': ['Zeratul'],
    'ZeratulDisruptor': ['Zeratul'],
    'ZeratulGateway': ['Zeratul'],
    'ZeratulHeroDarkArchon': ['Zeratul'],
    'ZeratulImmortal': ['Zeratul'],
    'ZeratulKhaydarinMonolith': ['Zeratul'],
    'ZeratulObserver': ['Zeratul'],
    'ZeratulPhotonCannon': ['Zeratul'],
    'ZeratulRoboticsFacility': ['Zeratul'],
    'ZeratulSentry': ['Zeratul'],
    'ZeratulStalker': ['Zeratul'],
    'ZeratulSummonKarass': ['Zeratul'],
    'ZeratulSummonZealot': ['Zeratul'],
    'ZeratulWarpPrism': ['Zeratul'],
    'ZeratulWarpPrismPhasing': ['Zeratul'],
    'ZeratulXelNagaConstruct': ['Zeratul'],
    'ZeratulXelNagaConstructCyan': ['Zeratul'],
    'Zergling': ['Zerg'],
    'ZerglingStetmann': ['Stetmann'],
}

KEY_ROWS = [
    ["6", "7", "8", "9", "0", "Minus", "Equals", "Backspace"],
    ["Y", "U", "I", "O", "P", "BracketOpen", "BracketClose", "BackSlash"],
    ["G", "H", "J", "K", "L", "SemiColon", "Apostrophe"],
    ["B", "N", "M", "Comma", "Period", "Slash"],
    ["Shift", "Alt", "Control"],
]
KEY_LABELS = {
    "Minus": "-", "Equals": "=", "Backspace": "⌫", "BracketOpen": "[",
    "BracketClose": "]", "BackSlash": "\\", "SemiColon": ";", "Apostrophe": "'",
    "Comma": ",", "Period": ".", "Slash": "/", "Grave": "`",
}
COMBOS = [
    ("plain", "plain"),
    ("Shift", "Shift"),
    ("Control", "Ctrl"),
    ("Alt", "Alt"),
    ("Control+Shift", "Ctrl+Shift"),
    ("Alt+Shift", "Alt+Shift"),
    ("Alt+Control", "Ctrl+Alt"),
    ("Alt+Control+Shift", "Ctrl+Shift+Alt"),
]


def parse_entries(path):
    """Yield (command, key, combo, raw) for every alternate in [Hotkeys]/[Commands].

    Same parse as tools/thecore_keys.py parse(), plus the raw `Command=Alt` line
    for the alternate so the page can show it.
    """
    section = None
    with open(path, encoding="utf-8-sig") as f:
        lines = f.read().splitlines()
    for line in lines:
        line = line.strip()
        if line.startswith("["):
            section = line
            continue
        if "=" not in line or section not in ("[Hotkeys]", "[Commands]"):
            continue
        cmd, val = line.split("=", 1)
        for alt in val.split(","):
            parts = [p for p in alt.split("+") if p]
            if not parts:
                continue
            base = [p for p in parts if p not in MODS]
            if base:
                key, mods = base[-1], [p for p in parts if p in MODS]
            else:
                # Modifier-only binding (CameraCenter=Alt): the last modifier is
                # the key, any others are held with it.
                key, mods = parts[-1], parts[:-1]
            combo = "+".join(sorted(mods)) or "plain"
            yield cmd, key, combo, "%s=%s" % (cmd, alt)


def factions_for(unit):
    """Faction names an entry with this unit belongs to."""
    if unit is None:
        return [GLOBAL]
    owners = UNIT_FACTIONS.get(unit)
    if not owners:
        return [UNCLASSIFIED]
    if len(owners) == 1 and owners[0] in MELEE:
        race = owners[0]
        return [race] + [c for c, r in COMMANDERS.items() if r == race]
    return list(owners)


def own_factions(unit):
    """Factions that own this unit outright in UNIT_FACTIONS, without race expansion."""
    if unit is None:
        return [GLOBAL]
    return list(UNIT_FACTIONS.get(unit) or [UNCLASSIFIED])


def build_file(path):
    idx = {f: i for i, f in enumerate(FACTIONS)}
    entries, unclassified, counts = [], set(), {f: 0 for f in FACTIONS}
    for cmd, key, combo, raw in parse_entries(path):
        ability, unit = (cmd.split("/", 1) + [None])[:2] if "/" in cmd else (cmd, None)
        facs = factions_for(unit)
        if facs == [UNCLASSIFIED]:
            unclassified.add(unit)
        for f in facs:
            counts[f] += 1
        entries.append([ability, unit or "", [idx[f] for f in facs], key, combo, raw,
                        [idx[f] for f in own_factions(unit)]])
    return entries, sorted(unclassified), counts


def main():
    data = {"factions": FACTIONS, "melee": MELEE, "commanders": COMMANDERS,
            "fingers": {k: sorted(v) for k, v in FINGERS.items()},
            "rows": KEY_ROWS, "labels": KEY_LABELS, "combos": COMBOS, "files": {}}
    order = []
    for name, rel in FILES:
        entries, unclassified, counts = build_file(os.path.join(HERE, rel))
        data["files"][name] = {"source": os.path.basename(rel), "entries": entries}
        order.append(name)
        print("%s: %d entries, %d unclassified units%s"
              % (name, len(entries), len(unclassified),
                 (": " + ", ".join(unclassified)) if unclassified else ""),
              file=sys.stderr)
        print("  " + "  ".join("%s=%d" % (f, counts[f]) for f in FACTIONS if counts[f]),
              file=sys.stderr)
    data["order"] = order
    html = TEMPLATE.replace("__DATA__", json.dumps(data, separators=(",", ":")))
    out = os.path.join(HERE, OUT)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote %s (%.0f KB)" % (OUT, os.path.getsize(out) / 1024.0), file=sys.stderr)


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<meta charset="utf-8">
<title>TheCore key map by race and co-op commander</title>
<style>
:root { --pinky:#e8d5f0; --ring:#d6e4f7; --middle:#d9f0d9; --index:#fbe6cf; --thumb:#f7d7d7; --other:#eceff1; }
* { box-sizing: border-box; }
body { margin: 0; padding: 16px 20px 40px; font: 14px/1.4 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1a1a1a; }
h1 { font-size: 20px; margin: 0 0 4px; }
p.lede { margin: 0 0 14px; color: #555; max-width: 90ch; }
.bar { border: 1px solid #ddd; border-radius: 6px; padding: 10px 12px; margin-bottom: 14px; background: #fafafa; }
.row { display: flex; flex-wrap: wrap; align-items: center; gap: 6px; margin-bottom: 8px; }
.row:last-child { margin-bottom: 0; }
.row b { font-size: 11px; text-transform: uppercase; letter-spacing: .06em; color: #666; width: 84px; flex: none; }
button.t { font: inherit; padding: 3px 9px; border: 1px solid #ccc; background: #fff; border-radius: 4px; cursor: pointer; }
button.t:hover { border-color: #888; }
button.t.on { background: #1f6feb; border-color: #1f6feb; color: #fff; }
input[type=text] { font: inherit; padding: 3px 8px; border: 1px solid #ccc; border-radius: 4px; width: 260px; }
select { font: inherit; padding: 3px; }
.legend { display: flex; gap: 10px; flex-wrap: wrap; font-size: 12px; color: #555; margin: 0 0 10px 0; }
.legend span { padding: 2px 8px; border-radius: 3px; border: 1px solid #0002; }
.kb { display: flex; flex-direction: column; gap: 6px; }
.krow { display: flex; gap: 6px; flex-wrap: wrap; }
.key { width: 148px; min-height: 92px; border: 1px solid #bbb; border-radius: 5px; padding: 4px 6px; cursor: pointer; overflow: hidden; }
.key:hover { border-color: #1f6feb; }
.key.dim { opacity: .35; }
.key .kn { font-weight: 600; display: flex; justify-content: space-between; }
.key .kn .c { font-weight: 400; color: #444; font-size: 11px; }
.key .e { font-size: 11px; color: #333; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.key .e u { color: #666; text-decoration: none; }
.key .more { font-size: 11px; color: #777; }
.f-pinky { background: var(--pinky); } .f-ring { background: var(--ring); } .f-middle { background: var(--middle); }
.f-index { background: var(--index); } .f-thumb { background: var(--thumb); } .f-other { background: var(--other); }
h2 { font-size: 13px; text-transform: uppercase; letter-spacing: .06em; color: #666; margin: 18px 0 6px; }
#panel { position: fixed; top: 0; right: 0; width: 420px; height: 100%; background: #fff; border-left: 1px solid #ccc; box-shadow: -4px 0 14px #0001; padding: 14px 16px; overflow: auto; display: none; }
#panel.open { display: block; }
#panel h3 { margin: 0 0 2px; font-size: 17px; }
#panel .sub { color: #666; margin: 0 0 12px; font-size: 12px; }
#panel .grp { font-size: 12px; text-transform: uppercase; letter-spacing: .05em; color: #1f6feb; margin: 12px 0 4px; border-bottom: 1px solid #eee; }
#panel .ent { margin-bottom: 6px; }
#panel .ent .a { font-weight: 600; }
#panel .ent .u { color: #555; }
#panel .ent code { display: block; font-size: 11px; color: #777; }
#close { float: right; }
</style>
<body>
<h1>TheCore key map</h1>
<p class="lede">Every binding in TheCore's hotkey files, on the key that presses it. Pick a file, then a melee race or a
co-op commander. Commander views show all melee units of that commander's race plus the commander's own units, so a
commander that lacks a unit still shows it; tick <em>commander-specific only</em> to drop the inherited ones.
Unit-less commands and everything in <code>[Hotkeys]</code> are Global and appear in every view. Click a key for the
full list.</p>

<div class="bar">
  <div class="row"><b>File</b><select id="file"></select><span id="src" style="color:#777;font-size:12px"></span></div>
  <div class="row"><b>Melee</b><span id="fac-melee"></span></div>
  <div class="row"><b>Co-op</b><span id="fac-coop"></span></div>
  <div class="row"><b>Other</b><span id="fac-other"></span></div>
  <div class="row"><b>Commander</b><label id="ownlab"><input type="checkbox" id="own"> commander-specific only</label></div>
  <div class="row"><b>Modifier</b><span id="mods"></span></div>
  <div class="row"><b>Search</b><input type="text" id="q" placeholder="ability or unit name"><span id="stat" style="color:#555"></span></div>
</div>
<div class="legend" id="legend"></div>
<div class="kb" id="kb"></div>
<h2 id="extrah">Other bound keys</h2>
<div class="kb" id="extra"></div>
<div id="panel"><button class="t" id="close">close</button><div id="pbody"></div></div>

<script>
var DATA = __DATA__;
var FAC = DATA.factions, GI = FAC.indexOf("Global"), UI = FAC.indexOf("Unclassified");
var fingerOf = {};
Object.keys(DATA.fingers).forEach(function (f) { DATA.fingers[f].forEach(function (k) { fingerOf[k] = f; }); });
var inRows = {};
DATA.rows.forEach(function (r) { r.forEach(function (k) { inRows[k] = 1; }); });

var state = { file: DATA.order[0], faction: "Terran", mod: "all", q: "", own: false };

function words(s) {
  return s.replace(/_/g, " ").replace(/([a-z0-9])([A-Z])/g, "$1 $2")
          .replace(/([A-Z]+)([A-Z][a-z])/g, "$1 $2").trim();
}
function label(k) { return DATA.labels[k] || k; }
function plural(n, word) { return n + " " + word + (n === 1 ? "" : "s"); }
function esc(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }

function visible(e) {
  var fi = FAC.indexOf(state.faction), f = e[2];
  if (state.faction === "Global") { if (f.indexOf(GI) < 0) return false; }
  else if (state.faction === "Unclassified") { if (f.indexOf(UI) < 0) return false; }
  else if (state.own && DATA.commanders[state.faction]) {
    // commander-specific only: the unit must be filed under this commander itself.
    if (e[6].indexOf(fi) < 0 && e[6].indexOf(GI) < 0) return false;
  }
  else if (f.indexOf(fi) < 0 && f.indexOf(GI) < 0) return false;
  if (state.q) {
    var q = state.q.toLowerCase();
    if ((e[0] + " " + e[1] + " " + words(e[0]) + " " + words(e[1])).toLowerCase().indexOf(q) < 0) return false;
  }
  return true;
}
function modOk(e) { return state.mod === "all" || e[4] === state.mod; }

function byKey(useMod) {
  var m = {};
  DATA.files[state.file].entries.forEach(function (e) {
    if (!visible(e)) return;
    if (useMod && !modOk(e)) return;
    (m[e[3]] = m[e[3]] || []).push(e);
  });
  return m;
}

function keyCell(k, list) {
  var f = fingerOf[k] || "other", n = list ? list.length : 0;
  var h = '<div class="key f-' + f + (n ? "" : " dim") + '" data-k="' + k + '" title="' + k + " · " + f + '">';
  h += '<div class="kn"><span>' + esc(label(k)) + '</span><span class="c">' + n + "</span></div>";
  var sorted = (list || []).slice().sort(function (a, b) { return a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0; });
  sorted.slice(0, 6).forEach(function (e) {
    h += '<div class="e" title="' + esc(e[5]) + '">' + esc(words(e[0])) +
         (e[1] ? ' <u>· ' + esc(words(e[1])) + "</u>" : "") + "</div>";
  });
  if (sorted.length > 6) h += '<div class="more">+' + (sorted.length - 6) + " more</div>";
  return h + "</div>";
}

function render() {
  // The commander-only filter is meaningless for a melee race, so clear it
  // instead of leaving the box ticked but disabled.
  var isCmd = !!DATA.commanders[state.faction];
  if (!isCmd && state.own) { state.own = false; }
  document.getElementById("own").checked = state.own;
  var m = byKey(true), all = DATA.files[state.file].entries;
  var shown = 0;
  Object.keys(m).forEach(function (k) { shown += m[k].length; });
  document.getElementById("stat").textContent = shown + " of " + plural(all.length, "binding");
  document.getElementById("src").textContent = DATA.files[state.file].source;
  var html = "";
  DATA.rows.forEach(function (r) {
    html += '<div class="krow">';
    r.forEach(function (k) { html += keyCell(k, m[k]); });
    html += "</div>";
  });
  document.getElementById("kb").innerHTML = html;
  var extras = [];
  all.forEach(function (e) { if (!inRows[e[3]] && extras.indexOf(e[3]) < 0) extras.push(e[3]); });
  extras.sort();
  var eh = '<div class="krow">';
  extras.forEach(function (k) { eh += keyCell(k, m[k]); });
  document.getElementById("extra").innerHTML = eh + "</div>";
  document.getElementById("extrah").style.display = extras.length ? "" : "none";
  Array.prototype.forEach.call(document.querySelectorAll(".key"), function (el) {
    el.onclick = function () { openKey(el.getAttribute("data-k")); };
  });
  Array.prototype.forEach.call(document.querySelectorAll("button.t[data-f]"), function (b) {
    b.className = "t" + (b.getAttribute("data-f") === state.faction ? " on" : "");
  });
  Array.prototype.forEach.call(document.querySelectorAll("button.t[data-m]"), function (b) {
    b.className = "t" + (b.getAttribute("data-m") === state.mod ? " on" : "");
  });
  document.getElementById("own").disabled = !isCmd;
  document.getElementById("ownlab").style.opacity = isCmd ? "1" : "0.45";
}

function openKey(k) {
  var m = byKey(true)[k] || [];
  var h = "<h3>" + esc(label(k)) + "</h3><p class=\"sub\">" + esc(k) + " · " +
          (fingerOf[k] || "other") + " · " + plural(m.length, "binding") + " · " + esc(state.faction) + "</p>";
  DATA.combos.forEach(function (c) {
    var list = m.filter(function (e) { return e[4] === c[0]; });
    if (!list.length) return;
    list.sort(function (a, b) { return a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0; });
    h += '<div class="grp">' + esc(c[1]) + " (" + list.length + ")</div>";
    list.forEach(function (e) {
      h += '<div class="ent"><span class="a" title="' + esc(e[0]) + '">' + esc(words(e[0])) + "</span>" +
           (e[1] ? ' <span class="u" title="' + esc(e[1]) + '">· ' + esc(words(e[1])) + "</span>" : "") +
           "<code>" + esc(e[5]) + "</code></div>";
    });
  });
  document.getElementById("pbody").innerHTML = h;
  document.getElementById("panel").className = "open";
  document.getElementById("close").onclick = function () { document.getElementById("panel").className = ""; };
}

function facButton(name) {
  return '<button class="t" data-f="' + esc(name) + '">' + esc(name) + "</button>";
}
function init() {
  var sel = document.getElementById("file");
  sel.innerHTML = DATA.order.map(function (n) { return "<option>" + n + "</option>"; }).join("");
  sel.onchange = function () { state.file = sel.value; render(); };
  var counts = {};
  DATA.order.forEach(function (n) {
    DATA.files[n].entries.forEach(function (e) { e[2].forEach(function (i) { counts[i] = 1; }); });
  });
  document.getElementById("fac-melee").innerHTML = DATA.melee.map(facButton).join(" ");
  document.getElementById("fac-coop").innerHTML = Object.keys(DATA.commanders).map(facButton).join(" ");
  var other = ["Global"];
  if (counts[UI]) other.push("Unclassified");
  document.getElementById("fac-other").innerHTML = other.map(facButton).join(" ");
  document.getElementById("mods").innerHTML = '<button class="t" data-m="all">All</button> ' +
    DATA.combos.map(function (c) { return '<button class="t" data-m="' + c[0] + '">' + c[1] + "</button>"; }).join(" ");
  Array.prototype.forEach.call(document.querySelectorAll("button.t[data-f]"), function (b) {
    b.onclick = function () { state.faction = b.getAttribute("data-f"); render(); };
  });
  Array.prototype.forEach.call(document.querySelectorAll("button.t[data-m]"), function (b) {
    b.onclick = function () { state.mod = b.getAttribute("data-m"); render(); };
  });
  var own = document.getElementById("own");
  own.checked = false;
  own.onchange = function () { state.own = !!own.checked; render(); };
  document.getElementById("q").oninput = function (ev) { state.q = ev.target.value; render(); };
  document.getElementById("legend").innerHTML = ["pinky", "ring", "middle", "index", "thumb", "other"]
    .map(function (f) { return '<span class="f-' + f + '">' + f + "</span>"; }).join("");
  render();
}
init();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
