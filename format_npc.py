import json
import csv
import json 


#1
# eevee, togepi, skitty, whismur, solosis
#2 - Curr Lev, 11, 13
#3
# elekid, 
#4, 12, 14
# impidimp
#5
# joltik
#6
#7
#8
#9
#10
#11
#12
#13
#14
#15


mons = [
    ('eevee', 'wander_normal', 'adaptability', ['baby_doll_eyes', 'quick_attack'], 10, 11, 0, 3),
    ('skitty', 'wander_crystal_normal', 'cute_charm', ['fake_out', 'copycat'], 10, 11, 0, 3),
    ('solosis', 'wander_normal', 'magic_guard', ['confusion', 'reflect'], 10, 11, 0, 3),
    ('togepi', 'wander_dumb', 'super_luck', ['metronome'], 10, 11, 0, 3),
    ('whismur', 'wander_normal', 'rattled', ['echoed_voice', 'round'], 10, 11, 0, 5),
        # ("jigglypuff", "wander_normal", "friend_guard", ["sing", "double_slap", "mimic"], 38, 39, 0, 1),
    # 2
    ("ralts", "wander_normal", "telepathy", ["disarming_voice", "teleport"], 11, 12, 1, 4),
    ("goomy", "wander_normal", '', ["water_gun", "absorb"], 11, 12, 1, 4),
    ("diglett", "wander_normal", "arena_trap", ["astonish", "sand_attack"], 11, 12, 1, 4),

    #3
    ("houndour", "wander_normal", '', ["ember", "smog", "leer"], 12, 13, 2, 5),
    ("beldum", "wander_normal", '', ["take_down"], 12, 13, 2, 5),
    ("hatenna", "wander_normal", "healer", ["play_nice", "life_dew"], 13, 14, 2, 6),
    # ("hatenna", "wander_normal", "healer", ["play_nice", "aromatic_mist"], 11, 12, 0, 1),

    # ("spinda", "wander_normal", "tangled_feet", ["supersonic", "teeter_dance"], 12, 13, 0, 1),
    #4
    ("noibat", "wander_normal", "telepathy", ["double_team", "gust"], 15, 16, 3, 7),
    ("zubat", "wander_normal", "", ["poison_fang"], 14, 15, 3, 5),
    ("swinub", "wander_normal", "", ["mud_bomb"], 14, 15, 3, 5),

    #5
    ("nickit", "thief_crystal", "stakeout", ["thief"], 16, 17, 4, 5),

    #by 14, 16
    #6
    ("spritzee", "wander_normal", "", ["fairy_wind"], 16, 17, 5, 10),
    ("joltik", "wander_normal", "unnerve", ["electroweb", "string_shot"], 15, 16, 5, 8),
    ("pikachu", "wander_normal", "", ["quick_attack", "round", "thunder_wave"], 16, 17, 5, 10),
    ("woobat", "wander_normal", "", ["heart_stamp", "attract"], 15, 16, 5, 8),

    #7, 17, 19
    ("chingling", "wander_normal", "", ["wish", "wrap", "ally_switch"], 18, 19, 6, 9),
    ("nickit", "thief_crystal", "stakeout", ["thief"], 16, 17, 6, 10), # ADD HIGHER WEIGHT
    # ("morelull", "retreater", "", ["sleep_powder", "leech_seed"], 17, 18, 6, 1),
    ("gothita", "wander_normal", "competitive", ["confusion", "fake_tears"], 18, 19, 6, 9),

    #8
    ("jigglypuff", "wander_normal", "friend_guard", ["baton_pass", "defense_curl", "round"], 20, 21, 7, 11),
    ("mime_jr", "wander_normal", "technician", ["mimic", "stored_power"], 21, 22, 7, 10),
    # ("chingling", "wander_normal", "", ["wish", "wrap", "ally_switch"], 70, 36, 0, 1),
    ("marill", "wander_normal", "thick_fat", ["rollout", "aqua_ring"], 20, 21, 7, 10),
    ("gulpin", "wander_normal", "liquid_ooze", ["sludge", "yawn"], 19, 20, 7, 10),

    #by 9, 18, 20
    ("morelull", "retreater", "", ["sleep_powder", "leech_seed"], 22, 23, 8, 10),
    ("bagon", "wander_normal", "", ["focus_energy", "scary_face", "ember"], 21, 22, 8, 10),
    ("meditite", "wander_normal", "pure_power", ["fake_out", "force_palm"], 21, 22, 8, 10),
    ("elekid", "wander_normal", "", ["thunder_punch", "leer"], 21, 22, 8, 10),
    # ("houndour", "wander_normal", '', ["ember", "smog", "leer"], 11, 12, 4, 7),
    # ("hatenna", "wander_normal", "healer", ["play_nice", "life_dew"], 11, 12, 2, 5),
    # ("hatenna", "wander_normal", "healer", ["play_nice", "aromatic_mist"], 11, 12, 0, 1),
    # ("jigglypuff", "wander_normal", "friend_guard", ["defense_curl",  "round"], 11, 12, 0, 1),

    #10 
    # 20, 22
    # 21, 23
    ("tinkatink", "wander_normal", "mold_breaker", ["baby_doll_eyes", "metal_claw", "covet"], 22, 23, 9, 12),
    ("aron", "wander_normal", "rock_head", ["metal_claw", "dig"], 22, 23, 9, 11),
    # ("sneasel", "wander_crystal_normal", "", ["taunt", "icy_wind", "fury_swipes"], 70, 36, 0, 1),

    #11
    ("luvdisc", "wander_normal", "", ["wish", "water_pulse", "round"], 23, 24, 10, 14),
    ("clauncher", "wander_normal", "mega_launcher", ["aqua_jet", "vice_grip"], 23, 24, 10, 13),
    ("tentacool", "wander_normal", "liquid_ooze", ["acid", "water_gun"], 23, 24, 10, 13),
    ("sneasel", "wander_crystal_normal", "", ["taunt", "icy_wind", "fury_swipes"], 23, 24, 10, 13),
    ("kirlia", "wander_normal", "telepathy", ["magical_leaf", "heal_pulse", "lucky_chant"], 23, 24, 10, 13),
    ("mareanie", "wander_normal", "limber", ["acid_spray"], 22, 23, 10, 13),

    #12
    ("porygon", "wander_crystal_normal", "analytic", ["conversion", "signal_beam", "charge_beam"], 24, 25, 11, 14),
    ("feebas", "wander_normal", "", ["scald", "splash", "tackle", "flail"], 22, 23, 11, 14),
    # ("chinchou", "wander_normal", "", ["volt_switch", "supersonic", "dazzling_gleam"], 22, 23, 11, 14),
    # ("vulpix", "wander_normal", "flash_fire", ["ember", "imprison"], 24, 25, 11, 14),
    ("baltoy", "wander_normal", "", ["mud_slap", "rock_tomb", "cosmic_power"], 24, 25, 11, 14),
    # ("bronzor", "wander_normal", "", ["imprison", "psywave"], 70, 36, 0, 1),

    #13
    ("volbeat", "wander_normal", "swarm", ["dazzling_gleam", "bug_buzz", "round"], 25, 26, 12, 15),
    ("illumise", "wander_normal", "prankster", ["wish", "encore", "sweet_scent"], 26, 27, 12, 15),
    ("emolga", "wander_normal", "static", ["volt_switch", "acrobatics"], 25, 26, 12, 15),
    ("dunsparce", "wander_normal", "serene_grace", ["take_down", "pursuit", "yawn"], 25, 26, 12, 15),
    # ("audino", "wander_normal", "", ["healing_wish", "after_you", "heal_bell"], 70, 36, 0, 1),

    # ("togetic", "wander_normal", "super_luck", ["nasty_plot", "baton_pass", "after_you"], 70, 36, 0, 1),

    # ("duosion", "wander_normal", "", ["light_screen", "psyshock"], 70, 36, 0, 1),

    #14
    ("swoobat", "wander_normal", "", ["air_cutter", "imprison"], 26, 27, 0, 1),
    ("onix", "wander_normal", "", ["bind", "rage", "rock_tomb"], 26, 27, 13, 15),
    ("togetic", "wander_normal", "", ["double_team", "baton_pass", "after_you", "ancient_power"], 27, 28, 13, 15),
    ("sableye", "wander_crystal_normal", "prankster", ["thief", "taunt", "shadow_claw"], 27, 28, 13, 16),


    #15, 27. 29
    # ("golbat", "wander_normal", "", ["mean_look", "venoshock"], 70, 36, 0, 1),
    # ("klefki", "wander_normal", "prankster", ["torment", "spikes", "imprison"], 28, 29, 14, 16),
    ("skarmory", "wander_normal", "sturdy", ["spikes", "metal_claw"], 27, 28, 0, 1),
    ("rhyhorn", "wander_normal", "rock_head", ["rock_blast", "bulldoze"], 27, 28, 14, 15),
    ("bronzor", "wander_normal", "levitate", ["psywave", "stored_power"], 29, 30, 14, 15),


    #16, 27. 29
    ("loudred", "wander_normal", "", ["uproar", "stomp", "round"], 29, 30, 15, 18),
    ("solrock", "wander_normal", "levitate", ["psyshock", "rock_slide", "stealth_rock"], 29, 30, 15, 18),
    ("lunatone", "wander_normal", "levitate", ["moonblast", "moonlight", "hypnosis"], 29, 30, 15, 18),
    ("swoobat", "wander_normal", "", ["air_cutter", "imprison"], 29, 30, 15, 18),
    ("chatot", "wander_normal", "", ["chatter", "round", "mimic"], 29, 30, 0, 1),
    ("spinda", "wander_normal", "tangled_feet", ["focus_punch", "teeter_dance"], 29, 30, 0, 1),
    ("relicanth", "wander_normal", "", ["dive", "ancient_power"], 29, 30, 0, 1),
    ("mr_mime", "wander_normal", "", ["baton_pass", "calm_mind", "telekinesis"], 29, 30, 0, 1),
    ("nosepass", "wander_normal", "sturdy", ["power_gem", "discharge"], 70, 36, 0, 1),
    ("tinkatuff", "wander_crystal_normal", "mold_breaker", ["knock_off", "fake_out", "play_rough"], 70, 36, 0, 1),

    #17
    ("wigglytuff", "wander_normal", "friend_guard", ["round", "wish", "disable", "double_slap"], 30, 31, 0, 1),
    ("espeon", "wander_normal", "magic_bounce", ["dazzling_gleam", "psybeam"], 30, 31, 0, 1),
    ("metang", "wander_normal", "clear_body", ["take_down", "zen_headbutt", "magnet_rise"], 30, 31, 0, 1),
    ("umbreon", "wander_normal", "synchronize", ["wish", "mean_look", "snarl"], 30, 31, 0, 1),
    ("gothorita", "wander_normal", "competitive", ["future_sight", "trick"], 31, 32, 0, 1),


    #18
    ("plusle", "wander_normal", "", ["shock_wave", "helping_hand", "wish"], 31, 32, 0, 1),
    ("minun", "wander_normal", "", ["electroweb", "thunder_wave", "baton_pass", "copycat"], 31, 32, 0, 1),
    ("golbat", "wander_normal", "", ["haze", "wing_attack"], 31, 32, 0, 1),
    ("hattrem", "wander_normal", "healer", ["life_dew", "disarming_voice", "aromatic_mist"], 70, 36, 0, 1),
    ("duosion", "wander_normal", "", ["reflect", "pain_split", "astonish"], 70, 36, 0, 1),
    ("murkrow", "wander_crystal_normal", "", ["pursuit", "foul_play", "taunt"], 31, 32, 0, 1),
    ("electabuzz", "wander_normal", "", ["thunder_punch", "low_kick", "screech"], 70, 36, 0, 1),


    #19
    ("shelgon", "wander_normal", "", ["dragon_breath", "scary_face", "thrash"], 70, 36, 0, 1),
    ("sliggoo", "wander_normal", "", ["dragon_breath", "acid_spray"], 70, 36, 0, 1),
    ("mawile", "wander_crystal_normal", "", ["iron_head", "play_rough"], 70, 36, 0, 1),
    ("audino", "wander_normal", "", ["healing_wish", "after_you", "helping_hand", "round"], 70, 36, 0, 1),
    ("lairon", "wander_normal", "rock_head", ["autotomize", "iron_head"], 70, 36, 0, 1),
    ("mr_mime", "wander_normal", "", ["baton_pass", "calm_mind", "round"], 70, 36, 0, 1),
    
    # ("claydol", "wander_normal", "levitate", ["heal_block", "teleport", "extrasensory"], 70, 36, 0, 1),

    #20
    ("togedemaru", "wander_normal", "iron_barbs", ["zing_zap", "tickle"], 70, 36, 0, 1),
    ("ledian", "wander_normal", "", ["comet_punch", "drain_punch", "wish", "safeguard"], 70, 36, 0, 1),
    ("porygon2", "wander_normal", "", ["conversion_2", "recover", "psybeam"], 70, 36, 0, 1),


    # FINAL SECTION
    #21
    ("exploud", "wander_normal", "", ["hyper_voice", "rest", "sleep_talk"], 70, 38, 0, 1),
    ("thievul", "thief_crystal", "stakeout", ["sucker_punch", "foul_play", "tail_slap", "thief"], 70, 36, 0, 1),
    ("carbink", "turret", "", ["power_gem", "dazzling_gleam"], 70, 36, 0, 1),
    ("milotic", "wander_normal", "marvel_scale", ["water_pulse", "recover", "disarming_voice"], 70, 36, 0, 1),
    ("delcatty", "wander_normal", "cute_charm", ["assist", "wish", "fake_out"], 70, 36, 0, 1),
    ("klefki", "wander_normal", "prankster", ["torment", "spikes", "imprison"], 28, 29, 14, 16),

    #22
    ("gardevoir", "wander_normal", "telepathy", ["wish", "moonblast", "psyshock"], 70, 36, 0, 1),
    ("weavile", "thief_crystal", "", ["beat_up", "thief"], 70, 36, 0, 1),
    ("azumarill", "wander_normal", "pure_power", ["belly_drum", "aqua_tail"], 70, 46, 0, 1),
    ("raichu", "wander_normal", "", ["psychic", "disarming_voice"], 70, 36, 0, 1), # alolan

    #23
    ("milotic", "wander_normal", "marvel_scale", ["water_pulse", "recover", "disarming_voice"], 70, 36, 0, 1),
    ("dugtrio", "wander_normal", "arena_trap", ["sucker_punch", "bulldoze"], 70, 36, 0, 1),
    ("reuniclus", "wander_normal", "", ["psychic", "recover", "ally_switch"], 70, 36, 0, 1),
    ("hatterene", "wander_normal", "healer", ["psybeam", "dazzling_gleam", "heal_pulse"], 70, 36, 0, 1),
    ("electivire", "wander_normal", "", ["thunder_punch", "cross_chop", "fire_punch"], 70, 36, 0, 1),
    
    # ("golbat", "wander_normal", "", ["mean_look", "venoshock"], 70, 36, 0, 1),
    # ("klefki", "wander_normal", "prankster", ["torment", "spikes", "imprison"], 28, 29, 14, 16),
    ("noivern", "wander_normal", "telepathy", ["boomburst", "whirlwind", "air_slash"], 60, 51, 20, 21),
    # ("jigglypuff", "wander_normal", "friend_guard", ["sing", "double_slap", "mimic"], 38, 39, 0, 1),
    # ("wigglytuff", "wander_normal", "friend_guard", ["round", "wish", "rollout"], 70, 36, 0, 1),
    # ("ralts", "wander_normal", "", ["growl", "teleport"], 70, 36, 0, 1),
    # ("kirlia", "wander_normal", "telepathy", ["magical_leaf", "heal_pulse", "lucky_chant"], 70, 36, 0, 1),
    # ("gardevoir", "wander_normal", "telepathy", ["wish", "moonblast", "psyshock"], 70, 36, 0, 1),
    # ("whismur", "wander_normal", "", ["echoed_voice", "round"], 70, 36, 0, 1),
    # ("loudred", "wander_normal", "/", ["uproar", "stomp", "round"], 70, 36, 0, 1),
    # ("exploud", "wander_normal", "", ["hyper_voice", "rest", "sleep_talk"], 70, 36, 0, 1),
    # ("togepi", "wander_dumb", "super_luck", ["metronome"], 70, 36, 0, 3),
    # ("togetic", "wander_normal", "super_luck", ["nasty_plot", "baton_pass", "after_you"], 70, 36, 0, 1),
    # ("togekiss", "wander_normal", "super_luck", ["air_slash", "aura_sphere"], 70, 36, 0, 1),
    # ("eevee", "wander_normal", "adaptability", ["swift", "baby_doll_eyes", "quick_attack"], 10, 11, 0, 3),
    # ("umbreon", "wander_normal", "synchronize", ["wish", "mean_look", "feint_attack"], 70, 36, 0, 1),
    # ("espeon", "wander_normal", "magic_bounce", ["dazzling_gleam", "psybeam"], 70, 36, 0, 1),
    # ("beldum", "wander_normal", "", ["take_down"], 70, 36, 0, 1),
    # ("metang", "wander_normal", "", ["take_down", "zen_headbutt"], 70, 36, 0, 1),
    ("metagross", "wander_normal", "", ["agility", "meteor_mash"], 70, 36, 0, 1),
    # ("murkrow", "wander_crystal_normal", "", ["pursuit", "assurance"], 70, 36, 0, 1),
    ("honchkrow", "wander_normal", "", ["pursuit", "night_slash", "wing_attack"], 70, 36, 0, 1),
    # ("sneasel", "wander_crystal_normal", "", ["taunt", "icy_wind", "fury_swipes"], 70, 36, 0, 1),
    ("weavile", "wander_crystal_normal", "", ["hone_claws", "night_slash", "thief"], 70, 36, 0, 1),
    # ("houndour", "wander_normal", "", ["ember", "smog", "leer"], 70, 36, 0, 1),
    ("houndoom", "wander_normal", "", ["dark_pulse", "flamethrower"], 70, 36, 0, 1),
    # ("mawile", "wander_crystal_normal", "", ["sucker_punch", "iron_head"], 70, 36, 0, 1),
    # ("skitty", "wander_crystal_normal", "cute_charm", ["fake_out", "copycat"], 70, 36, 0, 3),
    # ("delcatty", "wander_normal", "cute_charm", ["assist", "wish"], 70, 36, 0, 1),
    # ("baltoy", "wander_normal", "", ["mud_slap", "rock_tomb", "rapid_spin"], 70, 36, 0, 1),
    ("claydol", "wander_normal", "", ["heal_block", "teleport", "extrasensory"], 70, 36, 0, 1),
    # ("feebas", "wander_normal", "", ["scald", "splash", "tackle", "flail"], 70, 36, 0, 1),
    ("milotic", "wander_normal", "marvel_scale", ["water_pulse", "recover", "disarming_voice"], 70, 36, 0, 1),
    # ("bagon", "wander_normal", "", ["focus_energy", "scary_face", "ember"], 70, 36, 0, 1),
    # ("shelgon", "wander_normal", "", ["dragon_breath", "scary_face", "thrash"], 70, 36, 0, 1),
    # ("chatot", "wander_normal", "", ["boomburst", "mimic"], 70, 36, 0, 1),
    ("audino", "wander_normal", "", ["healing_wish", "after_you", "heal_bell"], 70, 36, 0, 1),
    ("noivern", "wander_normal", "", ["tailwind", "dragon_pulse"], 70, 36, 0, 1),
    # ("relicanth", "wander_normal", "", ["dive", "ancient_power"], 70, 36, 0, 1),
    # ("luvdisc", "wander_normal", "", ["wish", "agility", "draining_kiss"], 70, 36, 0, 1),
    # ("swoobat", "wander_normal", "", ["air_cutter", "imprison"], 70, 36, 0, 1),
    # ("togedemaru", "wander_normal", "iron_barbs", ["zing_zap", "tickle"], 70, 36, 0, 1),
    # ("morelull", "wander_normal", "", ["spore", "leech_seed"], 70, 36, 0, 1),
    # ("mareanie", "wander_normal", "", ["wide_guard", "acid_spray"], 70, 36, 0, 1),
    # ("onix", "wander_normal", "", ["rock_slide", "sand_tomb"], 70, 36, 0, 1),
    ("steelix", "wander_normal", "", ["stealth_rock", "bind"], 70, 36, 0, 1),
    # ("piloswine", "wander_normal", "", ["take_down", "ice_fang", "ice_shard"], 70, 36, 0, 1),
    # ("nickit", "thief_crystal", "stakeout", ["thief"], 70, 36, 0, 1),
    # ("thievul", "wander_crystal_normal_greedy", "stakeout", ["sucker_punch", "foul_play", "tail_slap", "thief"], 70, 36, 0, 1),
    # ("dreepy", "wander_normal", "", [], 70, 36, 0, 1),
    # ("drakloak", "wander_normal", "", [], 70, 36, 0, 1),
    # ("dragapult", "wander_normal", "", [], 70, 36, 0, 1),
    # ("clefable", "wander_normal", "", [], 70, 36, 0, 1),
    # ("clefairyu", "wander_normal", "", [], 70, 36, 0, 1),
    # ("dragapult", "wander_normal", "", [], 70, 36, 0, 1),
    # ("hatenna", "wander_normal", "healer", ["play_nice", "aromatic_mist"], 70, 36, 0, 1),
    # ("hattrem", "wander_normal", "healer", ["life_dew", "disarming_voice", "aromatic_mist"], 70, 36, 0, 1),
    # ("hatterene", "wander_normal", "healer", ["psybeam", "dazzling_gleam", "heal_pulse"], 70, 36, 0, 1),
    # ("zubat", "wander_normal", "", ["leech_life", "poison_fang"], 70, 36, 0, 1),
    # ("golbat", "wander_normal", "", ["toxic", "venoshock"], 70, 36, 0, 1),
    # ("golbat", "wander_normal", "", ["toxic", "venoshock"], 70, 36, 0, 1),
    ("crobat", "wander_normal", "", ["haze", "cross_poison", "wing_attack"], 70, 36, 0, 1),
    ("glimmora", "wander_normal", "corrosion", ["toxic_spikes", "rock_slide"], 70, 36, 0, 1),
    # ("clauncher", "wander_normal", "mega_launcher", ["aqua_jet", "vice_grip"], 70, 36, 0, 1),
    ("clawitzer", "wander_normal", "mega_launcher", ["aura_sphere", "water_pulse", "dragon_pulse"], 70, 36, 0, 1),
    # ("helioptile", "wander_normal", "", [], 70, 36, 0, 1),
    # ("heliolisk", "wander_normal", "", [], 70, 36, 0, 1),
    # ("espurr", "wander_normal", "", ["tickle", ""], 70, 36, 0, 1),
    # ("meowstic", "wander_normal", "", [], 70, 36, 0, 1),
    # ("spritzee", "wander_normal", "", ["fairy_wind", "misty_terrain", "draining_kiss"], 70, 36, 0, 1),
    ("impidimp", "wander_crystal_normal_greedy", "pickpocket", ["torment", "foul_play", "play_rough"], 70, 36, 0, 1),
    # ("zorua", "wander_normal", "", [], 70, 36, 0, 1),
    # ("zoroark", "wander_normal", "", [], 70, 36, 0, 1),
    # ("diglett", "wander_normal", "arena_trap", ["dig", "sand_attack"], 70, 36, 0, 1),
    ("dugtrio", "wander_normal", "arena_trap", ["sucker_punch", "bulldoze"], 70, 36, 0, 1),
    # ("pikachu", "wander_normal", "", ["quick_attack", "nuzzle", "agility"], 70, 36, 0, 1),
    # ("raichu", "wander_normal", "", ["psychic", "electric_terrain"], 70, 36, 0, 1), # alolan
    # ("mimikyu", "wander_normal", "", [], 70, 36, 0, 1),
    # ("elekid", "wander_normal", "", ["thunder_punch", "leer"], 70, 36, 0, 1),
    # ("electabuzz", "wander_normal", "", ["thunder_punch", "low_kick", "charge"], 70, 36, 0, 1),
    ("electivire", "wander_normal", "", ["thunder_punch", "ice_punch", "fire_punch"], 70, 36, 0, 1),
    # ("gulpin", "wander_normal", "liquid_ooze", ["sludge", "yawn"], 70, 36, 0, 1),
    ("swalot", "wander_normal", "liquid_ooze", ["sludge", "stockpile", "spit_up", "swallow"], 70, 36, 0, 1),
    # ("gothita", "wander_normal", "competitive", ["substitute", "fake_tears"], 70, 36, 0, 1),
    # ("gothorita", "wander_normal", "competitive", ["future_sight", "trick"], 70, 36, 0, 1),
    ("gothitelle", "wander_normal", "shadow_tag", ["flatter", "psych_up", "stored_power"], 70, 36, 0, 1),
    # ("ledian", "wander_normal", "", ["comet_punch", "drain_punch", "wish", "safeguard"], 70, 36, 0, 1),
    # ("solrock", "wander_normal", "", ["wonder_room", "psyshock", "stealth_rock"], 70, 36, 0, 1),
    # ("lunatone", "wander_normal", "", ["moonblast", "moonlight", "hypnosis"], 70, 36, 0, 1),
    # ("solosis", "wander_normal", "", ["confusion", "reflect"], 10, 11, 0, 3),
    # ("duosion", "wander_normal", "", ["light_screen", "psyshock"], 70, 36, 0, 1),
    ("reuniclus", "wander_normal", "", ["psychic", "recover", "ally_switch"], 70, 36, 0, 1),
    ("sableye", "thief_crystal", "prankster", ["thief", "shadow_claw"], 70, 36, 0, 1),
    ("girafarig", "wander_normal", "inner_focus", ["nasty_plot", "baton_pass", "agility", "stomp"], 70, 36, 0, 1),
    ("farigiraf", "wander_normal", "sap_sipper", [], 70, 36, 0, 1),
    # ("vulpix", "wander_normal", "flash_fire", ["ember", "extrasensory"], 70, 36, 0, 1),
    ("ninetales", "wander_normal", "flash_fire", ["flamethrower", "safeguard", "imprison", "extrasensory"], 70, 36, 0, 1),
    # ("joltik", "wander_normal", "", ["electroweb", "string_shot"], 70, 36, 0, 1),
    # ("marill", "wander_normal", "pure_power", ["rollout", "aqua_ring"], 70, 36, 0, 1),
    ("azumarill", "wander_normal", "pure_power", ["aqua_jet", "play_rough", "superpower"], 70, 46, 0, 1),
    # ("tentacool", "wander_normal", "liquid_ooze", [], 70, 36, 0, 1),
    ("tentacruel", "wander_normal", "liquid_ooze", ["haze", "poison_jab"], 70, 36, 0, 1),
    # ("skarmory", "wander_normal", "sturdy", ["spikes", "metal_claw"], 70, 36, 0, 1),
    # ("bronzor", "wander_normal", "", ["imprison", "gyro_ball"], 70, 36, 0, 1),
    ("bronzong", "wander_normal", "", ["imprison", "gyro_ball", "safeguard"], 70, 36, 0, 1),
    # ("meditite", "wander_normal", "pure_power", ["fake_out", "force_palm"], 70, 36, 0, 1),
    ("medicham", "wander_normal", "pure_power", ["fake_out", "force_palm", "ice_punch"], 70, 36, 0, 1),
    ("chingling", "wander_normal", "", ["wish", "wrap", "ally_switch"], 70, 36, 0, 1),
    # ("chimecho", "wander_normal", "", ["yawn", "wrap", "healing_wish"], 70, 36, 0, 1),
    # ("porygon", "wander_normal", "analytic", ["conversion", "signal_beam"], 70, 36, 0, 1),
    ("porygon2", "wander_normal", "", ["conversion_2", "recover", "psybeam"], 70, 36, 0, 1),
    ("porygon_z", "wander_normal", "", ["tri_attack", "signal_beam", "conversion", "conversion_2"], 70, 36, 0, 1),
    # ("tinkatink", "wander_normal", "mold_breaker", ["baby_doll_eyes", "astonish", "covet"], 70, 36, 0, 1),
    # ("tinkatuff", "wander_normal", "mold_breaker", ["rock_smash", "metal_claw", "slam"], 70, 36, 0, 1),
    ("tinkaton", "wander_normal", "mold_breaker", ["play_rough", "knock_off", "fake_out"], 70, 36, 0, 1),
    # ("emolga", "wander_normal", "static", ["volt_switch", "acrobatics"], 70, 36, 0, 1),
    # ("kadabra", "wander_normal", "", ["kinesis", "psybeam", "ally_switch"], 70, 36, 0, 1),
    # ("volbeat", "wander_normal", "static", ["struggle_bug"], 70, 36, 0, 1),
    # ("illumise", "wander_normal", "", ["wish", "encore"], 70, 36, 0, 1),
    # ("plusle", "wander_normal", "", ["nuzzle", "quick_attack", "helping_hand"], 70, 36, 0, 1),
    # ("minun", "wander_normal", "", ["electro_ball", "helping_hand", "trump_card"], 70, 36, 0, 1),
    # "dunsparce" is missing in the original list
    ("goomy", "wander_normal", "", ["water_gun", "absorb"], 70, 36, 0, 1),
    ("sliggoo", "wander_normal", "", ["dragon_breath", "acid_spray"], 70, 36, 0, 1),
    ("goodra", "wander_normal", "", ["dragon_pulse", "muddy_water"], 70, 36, 0, 1),
    ("klefki", "wander_normal", "prankster", ["torment", "draining_kiss"], 70, 36, 0, 1),
    # ("formantis", "wander_normal", "", [], 70, 36, 0, 1),
    # ("lurantis", "wander_normal", "", [], 70, 36, 0, 1),
    ("rhyhorn", "wander_normal", "rock_head", ["rock_blast"], 70, 36, 0, 1),
    ("rhydon", "wander_normal", "roch_head", ["scary_face", "drill_run"], 70, 36, 0, 1),
    # ("mr_mime", "wander_normal", "", ["baton_pass", "calm_mind"], 70, 36, 0, 1),
    ("poochyena", "wander_normal", "run_away", ["howl", "bite"], 70, 36, 0, 1),
    ("mightyena", "retreater", "rattled", ["thief", "embargo", "roar"], 70, 36, 0, 1),
    ("persian", "wander_crystal_normal_greedy", "limber", ["fake_out", "fury_swipes"], 70, 36, 0, 1),
    ("nosepass", "wander_normal", "sturdy", ["power_gem", "discharge"], 70, 36, 0, 1),
    ("probopass", "wander_normal", "sturdy", ["magnet_bomb", "block"], 70, 36, 0, 1),
    # ("haunter", "wander_crystal_normal", "", ["shadow_ball", "lick"], 70, 36, 0, 1),
    # ("aron", "wander_normal", "rock_head", ["metal_claw", "headbutt"], 70, 36, 0, 1),
    # ("lairon", "wander_normal", "rock_head", ["autotomize", "take_down"], 70, 36, 0, 1),
    ("aggron", "wander_normal", "rock_head", ["metal_burst", "autotomize", "headbutt"], 70, 36, 0, 1),
]

# valid_mons = set(["eevee", "togepi", "skitty", "whismur", "solosis"])

def create_mon(mon):
    name, tactic, ability, moves, min_lev, max_lev, min_floor, max_floor = mon[0], mon[1], mon[2], mon[3], mon[4], mon[5], mon[6], mon[7]
    base_structure = {
        "Spawn": {
        "Spawn": {
        "BaseForm": {
        "Species": name,
        "Form": 0,
        "Skin": "",
        "Gender": -1
        },
        "Level": {
        "Min": min_lev,
        "Max": max_lev
        },
        "SpecifiedSkills": moves,
        "Intrinsic": ability,
        "Tactic": tactic,
        "SpawnConditions": [],
        "SpawnFeatures": [
        {
        "$type": "PMDC.LevelGen.MobSpawnMovesOff, PMDC",
        "StartAt": len(moves),
        "Remove": False
        },
        {
        "$type": "PMDC.LevelGen.MobSpawnWeak, PMDC"
        }
        ]
        },
        "Role": 0
        },
        "Rate": 10,
        "Range": {
        "Min": min_floor,
        "Max": max_floor
        }
    }
    return base_structure

mons.sort(key=lambda item: (item[-2], item[0]))

out_file = open("encounters.json", "w") 
present = set()
result = []
for mon in mons:
    name = mon[0]
    min_lev = mon[4]
    if (min_lev < 50):
        result.append(create_mon(mon))
        present.add(name)
        print(str(mon) + ",")



# json.dump({"Encounters": ", ".join(order) }, out_file, indent = 4, separators=(',', ': ')) 
# print(len(mons))


with open('Data/Zone/wishmaker_cave.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)

data['Object']['Segments'][0]["ZoneSteps"][4]["Spawns"] = result

with open('Data/Zone/wishmaker_cave.json', 'w') as file:
    json.dump(data, file, indent=2) 

# csv_filename = 'out.csv'
# with open(csv_filename, mode='w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(["Name", "Tactic", "Ablity", "Move 1", "Move 2", "Move 3", "Move 4", "Min Lev", "Max Lev", "Min Floor", "Max Floor"])
#     for row in mons:
#         while len(row[3]) != 4:
#             row[3].append("")
#         csv_writer.writerow([row[0], row[1], row[2], *row[3], row[4], row[5], row[6], row[7]])


# out_file.close()