# src/run_album.py
# 베르테르의 거울 — 10-Track Album Batch Execution
# Uses existing suno_client.py to submit all tracks to Suno API

import json
import time
import os
import sys
from datetime import datetime
from suno_client import SunoClient

# ──────────────────────────────────────────────
# Album: 베르테르의 거울 (Werther's Mirror)
# ──────────────────────────────────────────────

ALBUM = {
    "title": "베르테르의 거울 (Werther's Mirror)",
    "tracks": [
        {
            "number": 1,
            "title": "윤곽 없는 사람",
            "style": "Solo female vocal / ambient folk × dream pop, 72 BPM, 3/4 waltz feel, D minor with suspended chords, delicate fingerpicked acoustic guitar plays sparse arpeggios with room echo, bowed cello provides a low sustained drone, soft brush percussion supports a gentle pulse underneath, ambient pad synthesizer plays evolving warm textures in the background, Rhodes piano provides occasional single-note punctuation, vocal texture stays intimate breathy whisper throughout with fragile vibrato on phrase endings, delivery is hesitant and searching as if speaking to an empty room, phrasing floats behind the beat with long pauses between lines, wide stereo reverb field with the vocal placed close and dry against distant wet instrumentation, minimal low-end warmth, crystalline high-frequency clarity, mix stays sparse and transparent like morning fog",
            "lyrics": """[Intro | Ambient Pad + Cello Drone | Energy: Low | Mood: Empty]
(instrumental — 4 bars breathing space)

[Verse 1 | Vocals: Breathy Whisper | Fingerpicked Guitar | Energy: Low]
거울 앞에 서도 안개뿐이야
손을 뻗으면 아무것도 없어
이름을 불러도 메아리뿐
윤곽 없는 사람이 웃고 있어

[Verse 2 | Vocals: Searching | Energy: Low-Medium]
하루를 살아도 형태가 없어
비 오는 날 물웅덩이처럼
누군가 밟고 지나가야만
내가 여기 있었다는 걸 알아

[Chorus | Vocals: Open Fragile | Cello Swell | Energy: Medium]
나를 사랑하라고 했지만
사랑할 내가 보이지 않았어
빈 액자 속에 넣을 얼굴이
아직 그려지지 않았어

[Outro | Guitar Fade | Whispered]
윤곽 없는 사람...
누군가 그려주길 기다려""",
            "instrumental": False
        },
        {
            "number": 2,
            "title": "당신이라는 빛",
            "style": "Female vocal with layered harmonies / indie pop × shoegaze, 96 BPM, 4/4 with bouncy eighth-note pulse, G major shifting to B-flat major on chorus, jangly electric guitar plays bright open chords with chorus pedal shimmer, synth bass provides a warm rounded low pulse, drum machine plays crisp snappy snare with tight reverb on two and four, glockenspiel plays high melodic accents on chorus, ambient shimmer pad supports the wide stereo background, vocal texture transitions from curious soft tone to surprised warmth on chorus, delivery carries wonder and nervous excitement, phrasing is slightly rushed as if breathlessly discovering, moderately wide mix with bright presence on guitar and vocal, short room reverb, light compression for energy, mix opens significantly at chorus with added width and sparkle",
            "lyrics": """[Verse 1 | Vocals: Curious Soft | Jangly Guitar | Energy: Medium-Low]
카페 창가에 앉은 너를 봤어
무심한 햇빛이 너만 비추더라
처음으로 색이 보였어
회색 세계에 물감이 번지듯

[Verse 2 | Vocals: Warming | Energy: Medium]
네가 웃을 때 나도 웃고 있었어
이유를 몰라서 무서웠어
이런 감정에 이름이 있을까
도서관을 다 뒤져도 답이 없는

[Pre-Chorus | Building Excitement | Glockenspiel Enters]
네 이름 세 글자가
나침반이 되는 기분

[Chorus | Vocals: Surprised Warmth | Full Band Shimmer | Energy: High-Medium]
당신이라는 빛이 들어와
어두운 방에 창이 생겼어
나도 모르던 내 벽에 걸린
그림자가 처음으로 춤을 춰

[Bridge | Vocals: Whispered Wonder]
이건 사랑일까
아니면 처음 느끼는 나일까

[Chorus | Repeat]
당신이라는 빛이 들어와
어두운 방에 창이 생겼어""",
            "instrumental": False
        },
        {
            "number": 3,
            "title": "네가 보는 나",
            "style": "Ethereal female vocal with occasional spoken word / alternative rock × art pop, 112 BPM, 4/4 driving pulse, E minor to G major modulation at chorus, overdriven electric guitar plays restrained power chords on verse then opens to full distortion on chorus, bass guitar provides a punchy eighth-note groove with slight overdrive, live drums play tight verse pattern then explosive fills into chorus, strings section supports dramatic ascending lines at pre-chorus, piano plays sparse octave hits for emphasis, vocal texture shifts from controlled speaking tone to powerful open chest voice on chorus, delivery conveys disbelief turning to emotional realization, phrasing is precise and declarative on verse then soaring and sustained on chorus, tight focused mix on verse expanding to wide cinematic spread on chorus, medium plate reverb, punchy low end, crisp cymbal presence",
            "lyrics": """[Verse 1 | Vocals: Controlled Speaking | Restrained Guitar | Energy: Medium]
너는 말했어, 네 눈이 예쁘다고
나는 웃었어, 농담인 줄 알았어
거울 속 내 눈은 항상 피곤했는데
네가 보는 나는 다른 사람 같아

[Verse 2 | Vocals: Building Conviction | Energy: Medium-High]
너는 말했어, 네 목소리가 좋다고
노래를 불러달라고 했지
한 번도 좋다는 말을 못 들었는데
네 앞에서 처음 입을 열었어

[Pre-Chorus | Strings Ascending | Energy: Rising]
네가 보는 내가
진짜 나일 수도 있을까

[Chorus | Vocals: Powerful Open | Full Band Explosion | Energy: High]
네가 보는 나를 나도 보고 싶어
네 눈에 비친 내 윤곽을 따라가
거울은 거짓말쟁이였어
너만이 진짜 나를 비춰줬어

[Bridge | Vocals: Raw Emotional | Piano + Strings]
평생 들었던 말은
"넌 부족해, 넌 모자라"
근데 너는 말했어
"넌 이미 충분해"

[Final Chorus | Soaring | Full Orchestra + Band]
네가 보는 나를 나도 믿어볼게
네 눈이라는 거울을 빌려서
처음으로 나를 그려본다
당신 덕분에, 윤곽이 생긴다""",
            "instrumental": False
        },
        {
            "number": 4,
            "title": "부드러운 연습",
            "style": "Warm female vocal with soulful runs / neo-soul × contemporary R&B, 84 BPM, 4/4 laid-back groove, A-flat major with jazz extensions and ninth chords, Rhodes electric piano plays smooth gospel-influenced chord voicings with tremolo, fingerstyle bass guitar provides a deep warm walking groove, programmed drums play a head-nod pattern with soft kick and crispy hi-hat, muted trumpet provides occasional breathy countermelody lines, backing vocals support soft ooh-aah harmonies on chorus, vocal texture is rich and warm chest voice with control runs and gentle melisma, delivery conveys learning and self-compassion with tender authority, phrasing sits comfortably in the pocket with subtle syncopation, intimate close-mic mix with warm low-mids emphasis, short plate reverb on vocal, analog tape warmth throughout, bass prominent in mix center",
            "lyrics": """[Verse 1 | Vocals: Warm Chest | Rhodes Piano | Energy: Medium-Low]
넌 내 손에 밴드를 붙여줬어
아무렇지 않게, 당연하다는 듯
그 작은 손길이 알려줬어
나도 나를 이렇게 대할 수 있다고

[Verse 2 | Vocals: Growing Confidence | Muted Trumpet Enters]
넌 내 실수에 웃어줬어
"괜찮아" 두 글자가 약처럼
그래서 연습해보는 거야
거울 보며 나에게 말해보는 거야

[Chorus | Vocals: Soulful Open | Full Groove | Energy: Medium]
부드러운 연습을 시작해
네가 나에게 했던 것처럼
"괜찮아, 잘하고 있어"
내가 나에게 속삭여본다

[Bridge | Vocals: Tender Spoken + Sung | Backing Harmonies]
여전히 어색해, 아직 서툴러
자기 자신한테 다정하기가
이렇게 어려운 줄 몰랐어
하지만 너를 보면서 배워가

[Chorus | Final | Energy: Medium-High]
부드러운 연습을 멈추지 않을게
네가 보여준 다정함을 교본 삼아
오늘도 나에게 말해본다
"너는 사랑받을 자격이 있어" """,
            "instrumental": False
        },
        {
            "number": 5,
            "title": "고백 연습장",
            "style": "Intimate female vocal / acoustic ballad × chamber pop, 66 BPM, 6/8 gentle sway, C major with minor fourth borrowings, nylon string classical guitar plays fingerpicked arpeggios with warm body resonance, solo violin provides a singing countermelody that weaves around the vocal, soft upright bass provides sparse pizzicato notes on downbeats only, minimal brushed snare plays on beats two and five for subtle pulse, celeste plays delicate high-register ornaments between vocal phrases, vocal texture is pure and unadorned with no vibrato on verse then gentle natural vibrato on chorus, delivery is confessional like reading a letter aloud alone in a room, phrasing is deliberate with each word carefully placed, very intimate close-mic recording feel with minimal reverb on vocal, wide natural room ambience on instruments, warm analog character, mix is centered and minimal leaving space for every breath",
            "lyrics": """[Intro | Nylon Guitar Arpeggio | Energy: Minimal | Mood: Private]
(instrumental — 4 bars, like opening a notebook)

[Verse 1 | Vocals: Reading Aloud | Classical Guitar Only | Energy: Low]
친애하는 나에게,
이 편지를 쓰는 건 처음이야
항상 남에게만 쓰던 편지를
오늘은 나에게 보내보려 해

[Verse 2 | Vocals: Confessional | Violin Enters | Energy: Low]
그동안 미안했어, 나에게
맨 마지막에 챙기고
맨 처음에 미워하고
제일 가혹한 심판관이었으니까

[Chorus | Vocals: Gentle Acceptance | Violin + Guitar | Energy: Medium-Low]
당신에게 고백하기 전에
나에게 먼저 고백해야 할 것 같아
나는 부족하지 않았어
다만 그걸 아무도 말해주지 않았을 뿐

[Bridge | Vocals: Whispered | Celeste Enters]
이 편지를 부치진 않을 거야
그냥 서랍에 넣어둘 거야
하지만 썼다는 것만으로도
나를 한 발짝 안아준 거니까

[Outro | Vocals: Humming | Guitar Fade]
(humming the chorus melody...)
친애하는 나에게...""",
            "instrumental": False
        },
        {
            "number": 6,
            "title": "거울의 정원",
            "style": "Female vocal with choir harmonies on chorus / indie folk × orchestral pop, 100 BPM, 4/4 with walking pace feel, D major with pastoral quality, acoustic guitar plays bright strummed pattern with capo shimmer, mandolin plays quick tremolo accents on off-beats, orchestral strings provide lush ascending phrases building through verses, wooden flute plays a pastoral melody interlude between sections, stomp-clap percussion provides an earthy organic rhythm, bass cello provides warm grounding notes on root movements, vocal texture is clear and projecting folk-style with natural resonance, delivery conveys wonder and gratitude like walking through a garden for the first time, phrasing is forward-moving and rhythmically engaged, wide natural open-air mix with depth perspective, strings placed behind vocal in mid-field, bright acoustic instruments up front, light spring reverb, warm sunlit tonal character",
            "lyrics": """[Verse 1 | Vocals: Clear Folk | Acoustic Guitar + Mandolin | Energy: Medium]
당신이 심어준 씨앗 하나가
내 안에서 뿌리를 내렸어
이름 모를 꽃이 피어나
거울 속 정원이 열리기 시작해

[Verse 2 | Vocals: Growing Wonder | Strings Enter | Energy: Medium]
칭찬 한 마디가 물이 되고
함께한 시간이 햇빛이 되어
시들었던 가지마다
새싹이 고개를 들어

[Pre-Chorus | Flute Interlude | Stomp-Clap Enters]
나도 몰랐어 이런 꽃이
내 안에 있었다는 걸

[Chorus | Vocals: Open Clear + Choir | Full Orchestra | Energy: High-Medium]
거울의 정원이 자라나
당신이라는 빛을 먹고서
가시투성이 땅이었던 나에게
봄이 왔어, 당신 덕분에 봄

[Bridge | Vocals: Tender | Flute + Acoustic Only]
아직 잡초도 많고
돌밭도 남아있지만
당신이 아름답다 말해준
그 한마디가 비료가 됐어

[Final Chorus | Vocals: Soaring + Choir | Full Band | Energy: High]
거울의 정원을 걸어가
당신과 나란히 이 길을 걸어
처음으로 나의 꽃을 꺾어
당신 머리에 꽂아줄게""",
            "instrumental": False
        },
        {
            "number": 7,
            "title": "사라질까 봐",
            "style": "Female vocal with processed doubled layers / dark pop × synthwave, 118 BPM, 4/4 pulsing electronic drive, F-sharp minor with chromatic tension, analog synthesizer plays a dark pulsating arpeggio pattern with filter sweeps, deep sub bass provides a menacing low-end throb on every downbeat, drum machine plays tight punchy kick and sharp clap with gated reverb, haunting bell synthesizer plays distant high-register melody echoes, distorted electric guitar provides textural noise swells in transitions, vocal texture is intimate but with electronic processing adding subtle pitch-shift doubling, delivery conveys rising anxiety and desperate questioning, phrasing starts controlled then accelerates into breathless urgency at chorus, claustrophobic close mix on verse opening to wide dramatic stereo sweep on chorus, heavy sidechain compression on synths against kick, metallic sheen on high frequencies, dark atmospheric depth",
            "lyrics": """[Intro | Pulsing Synth Arpeggio | Energy: Medium | Mood: Anxious]
(heartbeat-like synth pulse builds)

[Verse 1 | Vocals: Intimate Processed | Dark Synth | Energy: Medium]
밤마다 같은 꿈을 꿔
네가 등을 돌리는 꿈
거울이 깨지는 소리에 깨면
손에 쥔 건 빈 유리 조각뿐

[Verse 2 | Vocals: Rising Anxiety | Noise Swells | Energy: Medium-High]
네가 보여준 내가
너 없이도 존재할 수 있을까
혼자 남은 거울 앞에서
안개만 다시 차오르면 어쩌지

[Pre-Chorus | Vocals: Desperate Whisper | Bell Synth | Energy: Rising]
놓치면 안 돼, 놓으면 안 돼
이 거울만은 깨지면 안 돼

[Chorus | Vocals: Breathless Urgency | Full Electronic Wall | Energy: High]
사라질까 봐, 네가 사라질까 봐
그러면 나도 다시 안개가 될까 봐
당신 없는 거울에 비칠 내가
다시 윤곽 없는 사람일까 봐

[Bridge | Vocals: Broken Honest | Synth Drops to Pad | Energy: Low]
이건 사랑이 아니라
두려움인 걸 알아
하지만 두려움 안에서도
진짜 마음은 숨을 쉬고 있어

[Chorus | Vocals: Resolved | Rebuilding | Energy: High]
사라질까 봐, 그래도 말할게
당신이 없어도 나는 여기 있을게
깨진 거울 조각을 모아서
내 손으로 다시 붙여볼게""",
            "instrumental": False
        },
        {
            "number": 8,
            "title": "내 이름으로 서는 법",
            "style": "Powerful female vocal with raw energy / anthemic rock × post-punk revival, 132 BPM, 4/4 driving forward momentum, A major with triumphant power chord progressions, distorted electric guitar plays massive open chord riffs with aggressive strumming, second guitar plays high melodic lead lines with overdrive, punchy bass guitar provides a galloping eighth-note drive anchoring the groove, live drums play explosive fills and powerful four-on-the-floor kick, gang vocal chants support chorus hook in unison, tambourine plays constant eighth notes for texture and urgency, vocal texture is raw powerful belt with gritty edges and occasional controlled breaks, delivery conveys fierce determination and hard-won confidence, phrasing is rhythmically aggressive locking tight with the drum pattern, loud proud in-your-face mix with guitars wide and present, vocal cutting through the center, compressed punchy low end, bright aggressive high frequency excitement, arena-scale reverb on chorus",
            "lyrics": """[Intro | Guitar Riff + Drum Count In | Energy: High | Mood: Determined]
(explosive guitar riff — 4 bars)

[Verse 1 | Vocals: Raw Gritty | Driving Guitar | Energy: High]
더 이상 네 눈을 빌리지 않아
내 눈으로 나를 똑바로 볼 거야
부족해도 괜찮아, 그게 나야
완벽한 척 안 해도 나야

[Verse 2 | Vocals: Fierce | Full Band Drive | Energy: High]
네가 심어준 씨앗은 감사하지만
물을 주는 건 이제 내 몫이야
거울이 깨져도 나는 서 있어
조각 하나하나가 다 내 얼굴이야

[Pre-Chorus | Gang Vocals Enter | Energy: Rising to Peak]
이름을 불러봐, 내 이름을
내가 내 이름을 부를 차례야

[Chorus | Vocals: Powerful Belt + Gang Chant | Full Band + Tambourine | Energy: Peak]
내 이름으로 서는 법을 배웠어
당신이 보여줬고, 내가 걸어왔어
더 이상 빈 액자가 아니야
내 얼굴로, 내 이름으로, 나로 서 있어

[Bridge | Vocals: Quiet Honest → Building | Guitar Only | Energy: Medium → High]
고마워, 진심으로
네가 아니었으면 몰랐을 거야
하지만 이제 알았으니까
나는 나를 놓지 않을 거야

[Final Chorus | Vocals: Maximum Power | Everything Full | Energy: Peak]
내 이름으로 서는 법을 배웠어
넘어져도 내가 나를 일으켜
이건 너에 대한 사랑도 맞고
나에 대한 사랑도 맞아 — 둘 다야""",
            "instrumental": False
        },
        {
            "number": 9,
            "title": "베르테르의 고백",
            "style": "Female vocal building from intimate to orchestral climax / cinematic pop × orchestral ballad, 76 BPM, 4/4 with grand sweeping feel, E-flat major with rich harmonic movement, grand piano plays arpeggiated chords with sustain pedal bloom expanding through the song, full string orchestra provides sweeping emotional phrases and sustained harmonic beds, French horn plays a noble theme melody emerging at bridge, timpani provides dramatic punctuation at key moments, harp plays gentle glissando transitions between sections, subtle choir provides wordless harmonies on final chorus, vocal texture opens from intimate whisper to fully supported operatic chest belt on climax, delivery is the most emotionally exposed and vulnerable in the album, phrasing is patient and deliberate allowing every word maximum emotional weight, cinematic panoramic mix starting intimate then expanding to massive orchestral width, deep concert hall reverb, rich warm low frequencies, sparkling high-end clarity",
            "lyrics": """[Intro | Solo Piano | Energy: Low | Mood: The Most Important Confession]
(piano arpeggios — 8 bars, unhurried)

[Verse 1 | Vocals: Intimate Whisper | Piano Only | Energy: Low]
세상은 말했어
나를 먼저 사랑하라고
그래야 남을 사랑할 수 있다고
그래서 혼자 애를 썼어

[Verse 2 | Vocals: Growing | Strings Enter | Energy: Medium-Low]
텅 빈 거울 앞에서
자기 사랑을 연습했지만
사랑할 내가 보이지 않는데
어떻게 사랑하라는 거야

[Pre-Chorus | Vocals: Honest Pain | Strings Swell + French Horn | Energy: Medium]
그러다 당신을 만났어
모든 공식이 무너지는 순간

[Chorus | Vocals: Open Emotional | Full Orchestra | Energy: High]
당신을 사랑한 후에야
나를 사랑하게 되었어
순서가 틀렸다고 해도 괜찮아
이것이 나의 진실이니까

[Verse 3 | Vocals: Confessional | Piano + Cello | Energy: Medium]
당신이 보여준 내 모습 속에서
처음으로 사랑할 만한 나를 발견했어
베르테르의 편지처럼
격렬하고 또 서툰 이 고백

[Chorus | Vocals: Full Voice | Full Orchestra + Choir | Energy: High]
당신을 사랑한 후에야
나를 사랑하게 되었어
거울이 아니라 당신이었어
나를 비춰준 건 처음부터 당신이었어

[Bridge | Vocals: Maximum Vulnerability | Harp + Timpani | Energy: Peak Build]
이 말을 하기까지
십 년이 걸렸어
나를 사랑하지 못하는 사람이
감히 사랑을 말해도 되냐고

근데 이제 알아
사랑은 자격이 아니야
당신이 나를 사랑해줬고
그 사랑이 나를 깨웠어

[Final Chorus | Vocals: Operatic Climax | Everything | Energy: Maximum]
당신을 사랑한 후에야
나를 사랑하게 되었어
순서 따윈 상관없었어
사랑이 먼저, 자격은 그 후에 온다""",
            "instrumental": False
        },
        {
            "number": 10,
            "title": "나라는 계절",
            "style": "Solo female vocal with breath sounds audible / ambient pop × minimalist piano epilogue, 60 BPM, free time feel with gentle rubato, F major with lydian brightness, solo grand piano plays simple chordal movement with long sustain and natural decay, soft ambient pad provides barely audible harmonic support, distant wind chimes play random gentle accents like a breeze, nature field recording provides subtle birdsong atmosphere underneath, vocal texture is completely natural unprocessed and intimate as if sitting beside the listener, delivery is peaceful and settled with no tension or urgency, phrasing is completely free and unhurried with natural breathing audible, extremely intimate recording with almost no reverb on vocal creating closeness, piano has natural room ambience, very quiet mix with dynamic subtlety, warm analog character throughout, the gentlest possible ending",
            "lyrics": """[Intro | Solo Piano | Energy: Minimal | Mood: Morning After Everything]
(piano — 8 bars, like the first day of a new season)

[Verse 1 | Vocals: Natural Intimate | Piano Only | Energy: Low]
창문을 열면 바람이 와
당신의 향기는 아니지만
내가 좋아하는 냄새를 알아
이제는 혼자서도

[Verse 2 | Vocals: Peaceful | Wind Chimes + Birdsong | Energy: Low]
거울 속에 사람이 서 있어
윤곽이 선명한 사람이
웃고 있어, 나한테 웃어
처음으로 거울이 따뜻해

[Chorus | Vocals: Gentle Open | Piano + Ambient Pad | Energy: Low-Medium]
나라는 계절이 왔어
당신이 심은 봄이 지나고
여름, 가을, 겨울을 지나
나만의 계절이 돌아왔어

[Bridge | Vocals: Whispered Gratitude]
고마워, 사랑했어
아니, 사랑하고 있어
당신이 떠나도 남는 건
당신이 피워준 나니까

[Outro | Vocals: Humming → Silence | Piano Fade | Energy: Minimal]
(humming quietly...)
나라는 계절...
(piano sustain fading into silence)
(birdsong continues alone — 4 bars)
(silence)""",
            "instrumental": False
        }
    ]
}

# ──────────────────────────────────────────────
# Execution
# ──────────────────────────────────────────────

def run_album():
    client = SunoClient()
    
    if not client.api_key:
        print("❌ SUNO_COOKIE 환경변수가 설정되지 않았습니다.")
        print("   .env 파일에 SUNO_COOKIE=your_api_key 를 추가하세요.")
        print("   API 키: https://sunoapi.org 에서 발급")
        sys.exit(1)
    
    print("=" * 60)
    print(f"🪞 앨범: {ALBUM['title']}")
    print(f"📀 트랙 수: {len(ALBUM['tracks'])}")
    print(f"⏰ 시작: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    results = []
    
    for track in ALBUM["tracks"]:
        print(f"\n{'─' * 50}")
        print(f"🎵 Track {track['number']:02d}: {track['title']}")
        print(f"   Style: {track['style'][:80]}...")
        print(f"   Lyrics: {len(track['lyrics'])} chars")
        print(f"   Instrumental: {track['instrumental']}")
        
        try:
            response = client.generate_music(
                prompt=track["lyrics"],
                style=track["style"],
                title=track["title"],
                instrumental=track["instrumental"],
                model="V5",
                custom_mode=True
            )
            
            if response and response.get("code") == 200:
                task_id = response.get("data", {}).get("taskId", "unknown")
                print(f"   ✅ Submitted! Task ID: {task_id}")
                results.append({
                    "track": track["number"],
                    "title": track["title"],
                    "task_id": task_id,
                    "status": "submitted"
                })
            else:
                print(f"   ⚠️ Unexpected response: {json.dumps(response, ensure_ascii=False)[:200]}")
                results.append({
                    "track": track["number"],
                    "title": track["title"],
                    "task_id": None,
                    "status": "error",
                    "response": str(response)[:200]
                })
                
        except Exception as e:
            print(f"   ❌ Exception: {e}")
            results.append({
                "track": track["number"],
                "title": track["title"],
                "task_id": None,
                "status": "exception",
                "error": str(e)
            })
        
        # Rate limit: wait between requests
        if track["number"] < len(ALBUM["tracks"]):
            print(f"   ⏳ Waiting 5 seconds before next track...")
            time.sleep(5)
    
    # Save results
    print(f"\n{'=' * 60}")
    print("📋 RESULTS SUMMARY")
    print(f"{'=' * 60}")
    
    results_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "music-system", "albums", "werthers_mirror_results.json"
    )
    
    for r in results:
        emoji = "✅" if r["status"] == "submitted" else "❌"
        print(f"  {emoji} Track {r['track']:02d}: {r['title']} — {r['status']} ({r.get('task_id', 'N/A')})")
    
    with open(results_path, "w", encoding="utf-8") as f:
        json.dump({
            "album": ALBUM["title"],
            "submitted_at": datetime.now().isoformat(),
            "results": results
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 Results saved to: {results_path}")
    print(f"⏰ 완료: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    run_album()
