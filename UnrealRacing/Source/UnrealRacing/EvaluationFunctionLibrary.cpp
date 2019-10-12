// Fill out your copyright notice in the Description page of Project Settings.

#include "EvaluationFunctionLibrary.h"

#include "GenomeData.h"
#include <PlatformFilemanager.h>
#include <GenericPlatformFile.h>
#include <FileHelper.h>
#include <PlatformFile.h>
#include <Misc/Paths.h>

void UEvaluationFunctionLibrary::SortPopulation(TArray<UGenomeData*> Array, TArray<UGenomeData*>& SortedArray)
{
	uint32 ArraySize = Array.Num();

	Array.Sort([](const UGenomeData& A, const UGenomeData& B)
	{
		return A.fitness < B.fitness;
	});

	SortedArray = Array;
}

void UEvaluationFunctionLibrary::WriteFitness(TArray<UGenomeData*> Population, int32 Generation)
{	
	FString JoinedStr;
	for (int i = 0; i < Population.Num(); i++) {
		UGenomeData* genome = Population[i];
		JoinedStr += FString::Printf(TEXT("%s %s\n"), *FString::FromInt(genome->genomeID), *FString::SanitizeFloat(genome->fitness));
	}

	FString filename;
	filename += TEXT("generation_");
	filename += *FString::FromInt(Generation);
	filename += TEXT(".csv");

	WriteToFile(filename, JoinedStr);
}

void UEvaluationFunctionLibrary::WriteToFile(FString filename, FString data)
{
	FString SaveDirectory = FString("C:/racing_evaluation");

	UE_LOG(LogTemp, Warning, TEXT("%s"), *SaveDirectory);
	IPlatformFile& PlatformFile = FPlatformFileManager::Get().GetPlatformFile();

	if (PlatformFile.CreateDirectoryTree(*SaveDirectory))
	{
		FString AbsoluteFilePath = SaveDirectory + "/" + filename;

		FFileHelper::SaveStringToFile(data, *AbsoluteFilePath);
	}
}
