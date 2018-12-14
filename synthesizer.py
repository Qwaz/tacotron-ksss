import argparse

from tacotron.utils import makedirs, str2bool
from tacotron.synthesizer import Synthesizer

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--load_path', required=True)
    parser.add_argument('--sample_path', default="samples")
    parser.add_argument('--text', required=True)
    parser.add_argument('--num_speakers', default=1, type=int)
    parser.add_argument('--speaker_id', default=0, type=int)
    parser.add_argument('--checkpoint_step', default=None, type=int)
    parser.add_argument('--is_korean', default=True, type=str2bool)
    config = parser.parse_args()

    makedirs(config.sample_path)

    synthesizer = Synthesizer()
    synthesizer.load(config.load_path, config.num_speakers, config.checkpoint_step)

    audio = synthesizer.synthesize(
            texts=[config.text],
            base_path=config.sample_path,
            speaker_ids=[config.speaker_id],
            attention_trim=False,
            isKorean=config.is_korean)[0]
