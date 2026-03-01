import os
import re

directories_to_scan = ['.', 'pages', 'posts']

# Build a map of all available .md files
md_files = {}
for d in directories_to_scan:
    if os.path.exists(d):
        for root, _, files in os.walk(d):
            # Skip hidden directories and docs
            if '/.' in root or root.startswith('.'):
                if root != '.':
                    continue
            if 'docs' in root:
                continue
            for file in files:
                if file.endswith('.md') or file.endswith('.qmd'):
                    name = file[:-3] # without extension
                    # full path relative to site root, e.g. /pages/VisCorresEM.html
                    # Or we can just link to .md and quarto will resolve it
                    # But wait, Quarto site root is /
                    # Let's map name.lower() to the relative path of the .md file from root
                    rel_path = os.path.relpath(os.path.join(root, file), '.')
                    if rel_path.startswith('./'):
                        rel_path = rel_path[2:]
                    
                    md_files[name.lower()] = '/' + rel_path
                    # Also map exact case
                    md_files[name] = '/' + rel_path

print("Found files:", md_files.keys())

# Let's define manual mappings for known non-matching files
manual_map = {
    'extreme_rainfall': '/pages/extreme_rainfall_prediction.md',
    'fast_xray_tb': '/pages/fast_xray_tb.md',
    'mas_fm': '/pages/FM_attention_sampling.md',
    'videosummrl': '/pages/artefact_suppression_heart.md', # Wait, need to check
    'unsupervised_us_video': '/pages/medical_imaging_selfsupervised.md',
    '2007.13123': '/pages/deep_mri_prior.md', # check 
    'rapidcmr': '/pages/rapid_cmr.md',
    'artifactmr': '/pages/artefact_suppression_heart.md', # check
    'dishumerrgt': '/pages/bianca.md', # check
    'salad': '/pages/anomaly_detectionXray.md',
    'deepppca': '/pages/Dual-resolution-corresponding-networks.md', # check
    'arl': '/pages/class_relations_hstorr.md',
    '2008.08145': '/pages/barking_up.md', # check
    'pnm_radar_based_localization': '/pages/radar_based_localization.md',
    '2007.13886': '/pages/peyman/indi.md', # check
    'drcn': '/pages/Dual-resolution-corresponding-networks.md',
    'jakab20': '/pages/jakob_macke.md',
    'genlmm': '/pages/Oatmar_hilliges.md',
    'learning_by_synthesis': '/pages/learning_by_synthesis_gaze_2014.md',
    'gaze': '/pages/gaze_estimation.md',
    'defm_2016': '/pages/deep_eye_fm_2016.md',
    'hgsm': '/pages/hgsm_2018.md',
    'sm_dae': '/pages/score/sm_dae.md',
    'ssm': '/pages/score/sliced_sm.md',
    'ddpm': '/pages/score/ddpm.md',
    'smld': '/pages/score/smld.md',
    'score-matching': '/pages/score/score_matching.md',
    'multiscale-deblurring': '/pages/peyman/multiscale_deblurring.md',
    'indi': '/pages/peyman/indi.md'
}

def resolve_link(link_path):
    # Remove leading/trailing slashes
    clean_path = link_path.strip('/')
    
    # Check if exact match exists in keys
    base_name = os.path.basename(clean_path).lower()
    
    if link_path.strip('/') in manual_map:
        return manual_map[link_path.strip('/')]
    if base_name in manual_map:
        return manual_map[base_name]

    if base_name in md_files:
        return md_files[base_name]
    
    # Try just the clean path
    if clean_path in md_files:
        return md_files[clean_path]
    if clean_path.lower() in md_files:
        return md_files[clean_path.lower()]
        
    # Check if it's already an existing file
    if os.path.exists(clean_path):
        return '/' + clean_path
    
    if os.path.exists(clean_path + '.md'):
        return '/' + clean_path + '.md'
    
    return None

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find links: [text](/path/)
    # We want to be careful not to match http links
    def link_replacer(match):
        text = match.group(1)
        href = match.group(2)
        
        if href.startswith('http') or href.startswith('#') or href.startswith('mailto:'):
            return match.group(0)
            
        # If it's a relative path to a local file, like /VisCorresEM/
        new_href = resolve_link(href)
        if new_href:
            # print(f"Replacing {href} -> {new_href}")
            # If we want Quarto to resolve them perfectly from anywhere, we can use absolute paths with trailing .md
            # Quarto will render them to corresponding .html files
            # But wait, Quarto absolute paths (starting with /) resolve from the project root.
            return f"[{text}]({new_href})"
        else:
            print(f"COULD NOT RESOLVE: {href} in {file_path}")
            return match.group(0)

    new_content = re.sub(r'\[([^\]]+)\]\((/[^\)]+)\)', link_replacer, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            print(f"Updated links in {file_path}")

for d in directories_to_scan:
    if os.path.exists(d):
        for root, _, files in os.walk(d):
            if '/.' in root or root.startswith('.'):
                if root != '.':
                    continue
            if 'docs' in root:
                continue
            for file in files:
                if file.endswith('.md') or file.endswith('.qmd'):
                    process_file(os.path.join(root, file))
