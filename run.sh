#!/bin/bash
#SBATCH -J gpt2_training
#SBATCH -o ./training_outputs/shake_train%j.out
#SBATCH -e ./training_errors/shake_train%j.err
#SBATCH --gres=gpu:4
#SBATCH --gpus-per-node=4
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --mem=0
#SBATCH --time=9:33:33
#SBATCH --exclusive

module load cuda/11.8

#activate environment
source ~/miniforge3/envs/gpt2_env2.0/bin/activate
source activate

srun python run_clm.py \
    --model_type gpt2 \
    --tokenizer_name gpt2 \
    --train_file ./shake_gpt2_train.txt \
    --per_device_train_batch_size 32 \
    --per_device_eval_batch_size 32 \
    --do_train \
    --do_eval \
    --output_dir /tmp/test-clm \
    --overwrite_output_dir True \
    --num_train_epochs 100 \
    --fp16 
    
